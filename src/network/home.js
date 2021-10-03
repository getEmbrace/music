import request from './index.js'

export function getMusicList(songName){
  return request({
    url: '/getMusicList',
    method: 'post',
    data: {
      songName
    }
  })
}
export function getSongPic(songId){
  return request({
    url: '/getSongPic',
    method: 'post',
    data: {
      songId
    }
  })
}
export function getSongWord(songId){
  return request({
    url: '/getSongWord',
    method: 'post',
    data: {
      songId
    }
  })
}
export function getSongUrl(songId){
  return request({
    url: '/getSongUrl',
    method: 'post',
    data: {
      songId
    }
  })
}