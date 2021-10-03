<template>
  <div id="app">
    <div class="bg">
      <img :src="$store.state.songInfo.pic" alt="" />
    </div>
    <div class="mask_app"></div>
    <Home v-show="!isLyric"></Home>
    <Lyric v-show="isLyric"></Lyric>
    <Banner @songMenu_click="songMenu_click"></Banner>
    <SongList v-show="isSongList" @back_click="back_click"></SongList>
  </div>
</template>

<script>
import Home from "views/Home/Home.vue";
import Lyric from 'views/Lyric/Lyric.vue';
import Banner from "components/content/Banner.vue";
import SongList from "views/SongList/SongList.vue";

export default {
  name: "App",
  components: {
    Home,
    Banner,
    SongList,
    Lyric
  },
  data() {
    return {
      isSongList: false,
      isLyric: false
    };
  },
  methods: {
    songMenu_click() {
      this.isSongList = true;
    },
    back_click() {
      this.isSongList = false;
    },
  },
  mounted() {
    this.$bus.$on('isLyricChange', ()=> {
      this.isLyric = !this.isLyric;
    })
  },
};
</script>


<style>
@import "assets/css/base.css";
body {
  background-color: rgba(36, 34, 34, 0.562);
}
#app .bg {
  position: absolute;
  top: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  z-index: -1000;
}
#app .mask_app {
  position: absolute;
  top: 0;
  width: 100vw;
  height: 100vh;
  background-color: #000;
  opacity: 0.1;
  z-index: -999;
}
#app .bg img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  filter: blur(80px);
  width: 200%;
  height: 200%;
  
}
</style>
