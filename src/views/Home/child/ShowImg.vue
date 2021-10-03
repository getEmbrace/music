<template>
  <div class="showImg">
    <div class="waiper" >
      <img :src="songImg" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: "ShowImg",
  props: {
    songImg: {
      type: String,
      default: ""
    }
  },
  data(){
    return {
      rotate: 0,
      timer: null,
    }
  },
  methods: {
    musicStart(){
      let waiper = document.querySelector('.showImg').querySelector('.waiper')
      let img = waiper.querySelector('img');
      this.timer = setInterval(()=> {
        if(this.rotate >= 360){
          this.rotate = 0
        }
        img.style.transform = "rotate(" + this.rotate + "deg) translateZ(0)";
        this.rotate += 0.5;
      }, 50)
    },
    musicPause(){
      clearInterval(this.timer);
      this.timer = null;
    },
  },
  mounted(){
    this.$bus.$on("musicStart", ()=> {
      this.musicPause();
      this.musicStart();
      this.$store.commit('setSongInfo_status', true)
    })
    this.$bus.$on("musicPause", ()=> {
      this.musicPause()
      this.$store.commit('setSongInfo_status', false)
    })
  },
  created(){
  }
}
</script>

<style>
.showImg {
  position: relative;
  width: 100vw;
  height: 45vh;
  overflow: hidden;
}
.waiper {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -45%);
  width: 65vw;
  height: 65vw;
  overflow: hidden;
  border: 5px solid rgba(224, 224, 224, 0.5);
  border-radius: 50%;
}
.waiper img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}
</style>