<template>
  <div class="home">
    <ShowImg :songImg="songImg"></ShowImg>
    <SongInfo :songWord="songWord"></SongInfo>
  </div>
</template>

<script>
import ShowImg from './child/ShowImg.vue'
import SongInfo from './child/SongInfo.vue'

import {getSongPic, getSongWord, getSongUrl} from 'network/home.js'

export default {
  name: 'Home',
  components: {
    ShowImg,
    SongInfo,
  },
  data(){
    return {
      songList: [],
      songImg: "",
      songWord: ""
    }
  },
  methods: {
    getSongPic_h(songId){
      getSongPic(songId).then((info) => {
        let songInfo = JSON.parse(info.replace(/'/g, '"').replace(/True/g, 'true').replace(/False/g, 'false'))
        this.$store.commit('setSongInfo_pic', songInfo.songPic)
        this.songImg = songInfo.songPic
      })
    },
    getSongWord_h(songId){
      getSongWord(songId).then((info) => {
        this.songWord = info
      })
    },
    getSongUrl_h(songId){
      getSongUrl(songId).then((info) => {
        let songInfo = JSON.parse(info.replace(/'/g, '"').replace(/True/g, 'true').replace(/False/g, 'false'))
        this.$store.commit('setSongInfo_songUrl', songInfo.songUrl)
        this.$bus.$emit('setAudioSrc', songInfo.songUrl)
        if(songId){
          // 判断是否为点击触发（点击触发制动播放）
          this.$bus.$emit('songingChange');
        }
      })
    }
  },
  mounted(){
    this.$bus.$on("getSongInfoById", (songId) => {
      this.getSongPic_h(songId);
      this.getSongWord_h(songId);
      this.getSongUrl_h(songId);
    })
  },
  created(){
    this.getSongPic_h();
    this.getSongWord_h();
    this.getSongUrl_h()
  }
}
</script>
