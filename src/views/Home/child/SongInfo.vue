<template>
  <div class="songInfo">
    <div class="title">
      <span>{{ $store.state.songInfo.name }}</span>
    </div>
    <div class="arther">
      <span>{{ $store.state.songInfo.ar }}</span>
    </div>
    <div class="songWord" @click="Lyric_click">
      <div class="word0" :class="{ style_word: word0_active }">
        <span>{{ word0 }}</span>
      </div>
      <div class="word1" :class="{ style_word: !word0_active }">
        <span>{{ word1 }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "songInfo",
  props: {
    songWord: {
      type: String,
      defalut: ""
    },
  },
  data() {
    return {
      lrc_list: [],
      currentWord_index: null,
      current_time: null,
      word0: "",
      word1: "",
      word0_active: true,
    };
  },
  watch: {
    //控制歌词变化
    currentWord_index() {
      if (!this.word0_active) {
        if (this.currentWord_index == this.lrc_list.length - 1) {
          this.word0 = this.lrc_list[this.currentWord_index].content;
        } else {
          this.word0 = this.lrc_list[this.currentWord_index].content;
          this.word1 = this.lrc_list[this.currentWord_index + 1].content;
        }
        this.word0_active = !this.word0_active;
      } else {
        if (this.currentWord_index == this.lrc_list.length - 1) {
          this.word1 = this.lrc_list[this.currentWord_index].content;
        } else {
          this.word1 = this.lrc_list[this.currentWord_index].content;
          this.word0 = this.lrc_list[this.currentWord_index + 1].content;
        }
        this.word0_active = !this.word0_active;
      }
      this.$bus.$emit('currentSongWordChange', this.currentWord_index)
    },
    //将监听歌曲播放进度
    current_time() {
      for (let i in this.lrc_list) {
        if (this.current_time >= this.lrc_list[i].time) {
          this.currentWord_index = Number(i);
        }
      }
    },
    songWord() {
      //解析歌词
      if(this.songWord == ""){
        return
      }
      this.current_time = null;
      this.lrc_list = [];
      let lrc = this.songWord.split(/\n/g);
      for (let i of lrc) {
        let str = i.split(/\[(.*?)\](.*?)/);
        if (str.length == 4 && str[3] != "") {
          let time = str[1].split(":", 2);
          this.lrc_list.push({
            time: Number(time[0]) * 60 + Number(time[1]),
            content: str[3],
          });
        }
      }
      this.$store.commit('setSongWord', this.lrc_list)
      this.$bus.$emit('setLrcListss', this.lrc_list)
    },
  },
  methods: {
    Lyric_click(){
      this.$bus.$emit('isLyricChange')
    }
  },
  mounted() {
    //监听播放进度
    this.$bus.$on("current_time_change", (time) => {
      this.current_time = Number(time);
    });
    //初始化歌词
    this.current_time = 0.5;
  },
  created() {},
};
</script>

<style>
.style_word {
  color: #409eff !important;
}
.songInfo {
  margin-top: 30px;
  padding: 0 15px;
  width: 100vw;
  height: 30vh;
}
.songInfo .title {
  width: 90vw;
  font-size: 35px;
  font-weight: 500;
  color: #fff;
}
.songInfo .arther {
  margin-top: 10px;
  width: 90vw;
  font-size: 18px;
  color: rgba(255, 255, 255, 0.8)
}
.songWord {
  margin-top: 30px;
  width: 95vw;
  height: 10vh;
  transform: translateZ(0);
}
.songWord .word0 {
  font-size: 19px;
  color: rgba(255, 255, 255, 0.9)
}
.songWord .word1 {
  margin-top: 8px;
  font-size: 19px;
  color: rgba(255, 255, 255, 0.9)
}
</style>