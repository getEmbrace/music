<template>
  <div class="lyric">
    <div class="mask_lrc"></div>
    <div class="banner_lrc">
      <div class="back" @click="back_click">
        <i class="el-icon-back"></i>
      </div>
    </div>
    <div class="songInfo_lrc">
      <div class="title_lrc">
        <span>{{ $store.state.songInfo.name }}</span>
      </div>
      <div class="arther">
        <span>{{ $store.state.songInfo.ar }}</span>
      </div>
      <div class="songWord_lrc">
        <div class="words_lrc" v-for="(item, index) of lrcList" :key="index">
          <span>{{ item }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Lyric",
  data() {
    return {
      lrcList: [],
      lrcList_ss: [],
    };
  },
  methods: {
    back_click() {
      this.$bus.$emit("isLyricChange");
    },
    setLrcList(songIndex) {
      let list = [];
      for (let i = 0; i <= 5; i++) {
        if (songIndex - 5 + i < 0) {
          list.push("");
        } else {
          list.push(this.lrcList_ss[songIndex - 5 + i].content);
        }
      }
      for (let i = 6; i <= 10; i++) {
        if (songIndex + i - 5 >= this.lrcList_ss.length) {
          list.push("");
        } else {
          list.push(this.lrcList_ss[songIndex - 5 + i].content);
        }
      }
      this.lrcList = list;
    },
  },
  mounted() {
    this.$bus.$on("currentSongWordChange", (index) => {
      this.setLrcList(index);
    });
    this.$bus.$on("setLrcListss", (info) => {
      this.lrcList_ss = info;
    });
  },
};
</script>

<style>
.lyric {
  position: relative;
  width: 100vw;
  height: 100vh;
}
.lyric .mask_lrc {
  position: absolute;
  top: 0;
  width: 100vw;
  height: 100vh;
  background-color: #000;
  opacity: 0.2;
}
.banner_lrc {
  position: absolute;
  width: 100vw;
  height: 10vh;
}
.banner_lrc .back {
  position: absolute;
  width: 10vh;
  height: 10vh;
  text-align: center;
  line-height: 10vh;
  font-size: 30px;
  color: rgba(255, 255, 255, 0.822);
}
.lyric .songInfo_lrc {
  position: absolute;
  top: 10vh;
  left: 50%;
  transform: translateX(-50%);
  width: 100vw;
  height: 75vh;
}
.lyric .songInfo_lrc .title_lrc {
  margin: 0 auto;
  width: 95vw;
  height: 5vh;
  font-size: 28px;
  font-weight: 500;
  text-align: center;
  color: #fff;
}
.lyric .songInfo_lrc .arther {
  margin: 0 auto;
  width: 95vw;
  height: 3vh;
  font-size: 16px;
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
}
.lyric .songInfo_lrc .songWord_lrc {
  margin: 0 auto;
  width: 80vw;
  height: 64vh;
}
.songWord_lrc .words_lrc {
  padding-top: 10px;
  width: 100%;
  height: 5.2vh;
  text-align: center;
}
.songWord_lrc .words_lrc:first-child {
  margin-top: 2vh;
} 
.songWord_lrc .words_lrc span {
  transform: translateZ(0);
  font-size: 17px;
}
.songWord_lrc .words_lrc:nth-child(n) {
  color: rgba(255, 255, 255, 0.3);
}
.songWord_lrc .words_lrc:nth-child(n + 3) {
  color: rgba(255, 255, 255, 0.6);
}
.songWord_lrc .words_lrc:nth-child(n + 5) {
  color: rgba(255, 255, 255, 0.9);
}
.songWord_lrc .words_lrc:nth-child(6) span{
  font-size: 20px;
  color: #409eff;
}
.songWord_lrc .words_lrc:nth-child(n + 7) {
  color: rgba(255, 255, 255, 0.9);
}
.songWord_lrc .words_lrc:nth-child(n + 8) {
  color: rgba(255, 255, 255, 0.6);
}
.songWord_lrc .words_lrc:nth-child(n + 10) {
  color: rgba(255, 255, 255, 0.3);
}
</style>