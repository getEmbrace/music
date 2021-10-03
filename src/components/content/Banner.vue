<template>
  <div class="banner">
    <div class="slider">
      <div class="start">
        <span>{{ currentTime_s[0] }}</span>
        <span>{{ currentTime_s[1] }}:</span>
        <span>{{ currentTime_s[2] }}</span>
        <span>{{ currentTime_s[3] }}</span>
      </div>
      <div class="item">
        <el-slider
          v-model="slider_value"
          :show-tooltip="false"
          @change="sliderChange"
        ></el-slider>
      </div>
      <div class="end">
        <span>{{ durationTime_s[0] }}</span>
        <span>{{ durationTime_s[1] }}:</span>
        <span>{{ durationTime_s[2] }}</span>
        <span>{{ durationTime_s[3] }}</span>
      </div>
    </div>
    <div class="b_botton">
      <div class="child" @click="shoucang_click">
        <img v-if="shoucang_active" src="~assets/icon/shoucang.png" alt="" />
        <img v-else src="~assets/icon/shoucang_active.png" alt="" />
      </div>
      <div class="child" @click="lastSong">
        <img src="~assets/icon/shangyishoushangyige.png" alt="" />
      </div>
      <div class="child" @click="bofang_click">
        <img v-if="bofang_active" src="~assets/icon/bofang.png" alt="" />
        <img v-else src="~assets/icon/zanting.png" alt="" />
      </div>
      <div class="child" @click="nextSong">
        <img src="~assets/icon/xiayigexiayishou.png" alt="" />
      </div>
      <div class="child" @click="songMenu_click">
        <img src="~assets/icon/yinlecaidan_music-menu.png" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {
      shoucang_active: true,
      bofang_active: true,
      slider_value: 0,
      audio: null,
      audio_src: "",
      currentTime: 0,
      duration: 0,
      currentTime_s: ["0", "0", "0", "0"],
      durationTime_s: ["0", "0", "0", "0"],
      bofang_first: true,
    };
  },
  watch: {
    currentTime() {
      this.$bus.$emit("current_time_change", this.currentTime);
      //向上取整
      this.slider_value = Math.ceil((this.currentTime / this.duration) * 100);
      let mTime = parseInt(this.currentTime / 60);
      let sTime = parseInt(
        this.currentTime - parseInt(this.currentTime / 60) * 60
      );
      let mTime_0 = parseInt(mTime / 10);
      let mTime_1 = mTime - mTime_0 * 10;
      let sTime_0 = parseInt(sTime / 10);
      let sTime_1 = sTime - sTime_0 * 10;
      this.currentTime_s = [mTime_0, mTime_1, sTime_0, sTime_1];
    },
  },
  methods: {
    shoucang_click() {
      //检查是否已收藏
      let isCollect = false;
      this.$store.state.songCollect.forEach((el) => {
        if (this.$store.state.songInfo.id == el.id) {
          isCollect = true;
          return;
        }
      });
      let name = this.$store.state.songInfo.name;
      let ar = this.$store.state.songInfo.ar;
      let id = this.$store.state.songInfo.id;
      //是否应该加入收藏
      if (this.shoucang_active && isCollect == false) {
        this.$store.commit("pushItem_songCollect", { name, ar, id });
      } else if (!this.shoucang_active && isCollect == true) {
        this.$store.commit("delItem_songCollect", id);
      }
      this.$bus.$emit('resetSoucang_s')
      this.shoucang_active = !this.shoucang_active;
    },
    init_audio() {
      this.audio = new Audio();
      this.audio.ontimeupdate = () => {
        this.currentTime = this.audio.currentTime;
      };
      this.audio.oncanplay = () => {
        this.duration = this.audio.duration;
        let mTime = parseInt(this.duration / 60);
        let sTime = parseInt(this.duration - parseInt(this.duration / 60) * 60);
        let mTime_0 = parseInt(mTime / 10);
        let mTime_1 = mTime - mTime_0 * 10;
        let sTime_0 = parseInt(sTime / 10);
        let sTime_1 = sTime - sTime_0 * 10;
        this.durationTime_s = [mTime_0, mTime_1, sTime_0, sTime_1];
      };
      this.audio.onended = () => {
        this.bofang_active = !this.bofang_active;
        this.$bus.$emit("musicPause");
        //结束自动播放下一首
        this.nextSong()
      };
    },
    bofang_click() {
      if (this.audio_src == "") {
        return;
      }
      if (this.bofang_active) {
        if (this.bofang_first) {
          this.audio.src = this.audio_src;
          this.bofang_first = false;
        }
        let playPromise = this.audio.play();
        this.$bus.$emit("musicStart");
        if (playPromise) {
          playPromise
            .catch((e) => {
              console.log(e);
              this.bofang_first = true;
            })
            .then(() => {
              this.bofang_active = !this.bofang_active;
            });
        }
      } else {
        this.$bus.$emit("musicPause");
        this.audio.pause();
        this.bofang_active = !this.bofang_active;
      }
    },
    sliderChange(value) {
      this.audio.currentTime = (value * this.duration) / 100;
    },
    songMenu_click() {
      this.$emit("songMenu_click");
    },
    initSoucang() {
      //检查是否已收藏
      let isCollect = false;
      this.$store.state.songCollect.forEach((el) => {
        if (this.$store.state.songInfo.id == el.id) {
          isCollect = true;
          return;
        }
      });
      if(isCollect){
        this.shoucang_active = false
      }else {
        this.shoucang_active = true
      }
    },
    nextSong(){
      let currentId = 0
      this.$store.state.songCollect.forEach((el, index) => {
        if (this.$store.state.songInfo.id == el.id) {
          currentId = index + 1;
          return;
        }
      });
      if(currentId >= this.$store.state.songCollect.length){
        currentId = 0
      }
      this.$store.commit("setSongInfo_id", this.$store.state.songCollect[currentId].id);
      this.$store.commit("setSongInfo_name", this.$store.state.songCollect[currentId].name);
      this.$store.commit("setSongInfo_ar", this.$store.state.songCollect[currentId].ar);
      this.$bus.$emit("getSongInfoById", this.$store.state.songCollect[currentId].id);
    },
    lastSong(){
      let currentId = 0
      this.$store.state.songCollect.forEach((el, index) => {
        if (this.$store.state.songInfo.id == el.id) {
          currentId = index - 1;
          return;
        }
      });
      if(currentId < 0){
        currentId = this.$store.state.songCollect.length -1
      }
      this.$store.commit("setSongInfo_id", this.$store.state.songCollect[currentId].id);
      this.$store.commit("setSongInfo_name", this.$store.state.songCollect[currentId].name);
      this.$store.commit("setSongInfo_ar", this.$store.state.songCollect[currentId].ar);
      this.$bus.$emit("getSongInfoById", this.$store.state.songCollect[currentId].id);
    }
  },
  mounted() {
    //初始化audio控件
    this.init_audio();
    //切换歌曲
    this.$bus.$on("songingChange", () => {
      this.bofang_first = true;
      this.bofang_active = true;
      this.initSoucang()
      this.bofang_click();
    });
    //切换歌曲
    this.$bus.$on("setAudioSrc", (src) => {
      this.audio_src = src;
    });
    //收藏状态初始化
    this.initSoucang()
    this.$bus.$on("resetSoucang", () => {
      this.initSoucang()
    })
  },
};
</script>

<style>
.banner {
  position: fixed;
  bottom: 0;
  width: 100vw;
  height: 15vh;
}
.slider {
  position: absolute;
  top: 0;
  width: 95vw;
  height: 5vh;
  margin: 0 auto;
  margin-left: 10px;
  color: rgba(255, 255, 255, 0.7);
}
.slider .start {
  position: absolute;
  left: 0;
  padding: 0 8px 0 0;
  width: 45px;
  height: 5vh;
  font-size: 15px;
  line-height: 5vh;
}
.slider .end {
  position: absolute;
  right: 0;
  padding: 0 0 0 8px;
  width: 45px;
  height: 5vh;
  line-height: 5vh;
}
.slider .item {
  position: absolute;
  left: 48px;
  width: calc(95vw - 90px);
}
.b_botton {
  position: absolute;
  top: 4vh;
  display: flex;
  justify-content: center;
  width: 100%;
  height: 10vh;
}
.b_botton .child {
  width: 10vh;
  height: 10vh;
  padding: 2vh;
}
.b_botton img {
  width: 100%;
  height: 100%;
}

</style>