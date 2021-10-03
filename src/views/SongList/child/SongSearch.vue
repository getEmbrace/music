<template>
  <div class="songSearch">
    <div class="searchInput">
      <div class="input">
        <input type="text" v-model="searchName">
        <i class="el-icon-search"></i>
      </div>
      <div class="title" @click="search_click">
        <span>搜索</span>
      </div>
    </div>
    <div class="songList_s">
      <ShowList :songData="songData" :isSearch="true" v-if="songData.length != 0"></ShowList>
      <div class="empty" v-else>
        <img src="~assets/img/empty.gif" alt="">
        <i v-if="searching" class="el-icon-loading"></i>
      </div>
    </div>
  </div>
</template>

<script>
import ShowList from './ShowList.vue'
import { getMusicList} from 'network/home.js'
export default {
  name: "SongSearch",
  components: {
    ShowList
  },
  data(){
    return {
      songData: [],
      searchName: "",
      searching: false
    }
  },
  methods: {
    getMusicList_h(songName){
      getMusicList(songName).then((info)=> {
        this.songData = JSON.parse(info.replace(/'/g, '"'))
        this.searching = false
      }).catch((e)=> {
        this.searching = false
      })
    },
    search_click(){
      if(this.searchName !== ""){
        this.songData = []
        this.searching = true
        this.getMusicList_h(this.searchName)
      }
    }
  }
}
</script>

<style>
.songSearch {
  width: 100%;
}
.searchInput {
  display: flex;
  padding-left: 50px;
  padding-bottom: 5px;
  width: 100vw;
  height: 45px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.13);
}
.searchInput .input {
  position: relative;
  flex: 1;
}
.searchInput .input input{
  width: 100%;
  height: 100%;
  outline: none;
  border: none;
  border-radius: 20px;
  padding-left: 35px;
  background-color: rgba(243, 231, 231, 0.514);
}
.searchInput .input i {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 20px;
}
.searchInput .title {
  margin: 0 5px;
  margin-right: 10px;
  width: 45px;
  height: 40px;
  text-align: center;
  line-height: 40px;
  font-size: 19px;
  color: black;
}
.songList_s {
  height: calc(70vh - 95px);
  overflow: auto;
}
.songList_s .empty {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #F7F7F7;
  overflow: hidden;
}
.songList_s .empty img{
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 100vw;
  transform: translate(-30%);
  font-size: 50px;
}
.songList_s .empty i {
  position: absolute;
  top: 35%;
  left: 45%;
  transform: translate(-50%, -50%);
  font-size: 28px;
}
</style>