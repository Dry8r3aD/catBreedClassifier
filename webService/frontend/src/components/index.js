import Vue from "vue";
import upperFirst from "lodash/upperFirst";
import camelCase from "lodash/camelCase";

/*
  1. 목적
    - components 폴더 안에 있는 파일들을 전역적으로 등록시키기 위한 사전 작업

  2. 설명
    - https://kr.vuejs.org/v2/guide/components-registration.html 

    2-(1) 컴포넌트 설정을 가져온다.
    2-(2) 파스칼 표기법으로 이름을 가져온 후 폴더 위치와 무관하게 파일 이름 추출
    2-(3) 컴포넌트를 전역적으로 등록

  3. 추후 고려사항 
    - 한 번에 컴포넌트를 전체적으로 가져오는게 초반 페이지 로딩 속도를 저해하지 않을까    

*/

// eslint-disable-next-line no-undef
const requireComponent = require.context(
  // 컴포넌트들이 있는 폴더
  "@/components",
  // 하위 폴더까지 포함할 지 여부
  true,
  // vue 파일만 추출
  /\.vue$/
);

requireComponent.keys().forEach(fileName => {
  // 2-(1) 컴포넌트 설정을 가져온다.
  const componentConfig = requireComponent(fileName);
  // 2-(2) 파스칼 표기법으로 이름을 가져온 후 폴더 위치와 무관하게 파일 이름 추출
  const componentName = upperFirst(camelCase(fileName.replace(/^\.\//, "").replace(/\.\w+$/, "")));
  // 2-(3) 컴포넌트를 전역적으로 등록
  Vue.component(componentName, componentConfig.default || componentConfig);
});
