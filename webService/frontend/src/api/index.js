import axios from "axios";

/* < 매개변수 설명 >
     1. method : get,post,put,delete
     2. url : ip 를 제외한 뒷부분만 기재 ex) http://123.32.4.2/admin --> /admin
     3. token : cookie 에 저장되어 있는 token 사용
     4. data : json 형태로 기재 ex) {"email":"sadf@asc.com","pwd":"123"} */

export async function reqGet(url, data) {
  // 개발 환경인지 프로덕션 환경인지 구분
  const DOMAIN = process.env.VUE_APP_API_ENDPOINT;
  axios.defaults.baseURL = DOMAIN;

  try {
    let res = {};

    res = await axios.get(url, {
      params: data
    });

    // 200번대는 모두 성공
    if (res.status / 100 == 2) {
      return res.data;
    } else {
      console.error("Invalid status : " + res.status);
      return false;
    }
  } catch (err) {
    if (err.response) {
      console.error("Invalid status : " + err.response);
    }

    return false;
  }
}
export async function reqPost(url, data) {
  // 개발 환경인지 프로덕션 환경인지 구분
  const DOMAIN = process.env.VUE_APP_API_ENDPOINT;
  axios.defaults.baseURL = DOMAIN;

  try {
    let res = {};
    res = await axios.post(url, data);

    // 200번대는 모두 성공
    if (res.status / 100 == 2) {
      return res.data;
    } else {
      console.error("Invalid status : " + res.status);
      return false;
    }
  } catch (err) {
    if (err.response) {
      console.error("Invalid status : " + err.response);
    }

    return false;
  }
}
