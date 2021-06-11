<template>
  <v-container fluid class="pa-0">
    <section class="pt-0">
      <v-parallax dark height="500" src="@/assets/img/cat_bg.jpeg">
        <v-row wrap justify="center" align="center">
          <v-col class="text-center" cols="12">
            <v-btn
              color="black"
              dark
              rounded
              outlined
              large
              target="_blank"
              href="https://github.com/Dry8r3aD/catBreedClassifier"
            >
              <v-icon dark class="mr-2">
                mdi-github
              </v-icon>
              Git Hub Link
            </v-btn>
            <h1 class="header__title">
              Cat Breed Classification Program
            </h1>
            <div class="header__subTitle">
              2021 AI Class Final Test Project
            </div>
            <!-- <v-btn class="blue lighten-2 mt-50" dark large @click="test">
              Upload Picture
            </v-btn> -->
            <v-btn class="blue darken-3s mt-50" dark x-large href="#mainContent">
              Get Start
            </v-btn>
          </v-col>
        </v-row>
      </v-parallax>
    </section>

    <section>
      <v-row wrap justify="center" align="center">
        <v-col class="text-center" cols="12">
          <v-img height="300" contain src="@/assets/img/cat_img.png" />
        </v-col>
        <v-col class="text-center" cols="12">
          <vue-typer
            :text="enableCatBreedList"
            :repeat="Infinity"
            :shuffle="true"
            initial-action="typing"
            :pre-type-delay="200"
            :type-delay="70"
            :pre-erase-delay="1500"
            :erase-delay="50"
            erase-style="backspace"
            :erase-on-complete="false"
            caret-animation="solid"
          ></vue-typer>
          <h1 class="content__title" data-aos="fade">
            귀여운 우리집 고양이 품종은?
          </h1>
        </v-col>
      </v-row>
    </section>

    <section class="content__cardBox">
      <v-row align-content="center" justify="center">
        <v-col cols="12" sm="4" md="4" lg="3" xl="3">
          <v-card
            class="elevation-0 transparent"
            color="grey lighten-3"
            data-aos="fade-up"
            data-aos-delay="100"
            data-aos-duration="700"
          >
            <v-card-text class="text-center ma-auto">
              <div class="card__title">
                <v-icon x-large class="pb-4">mdi-cat</v-icon>
                <h1 class="headline text-xs-center pb-8">48 Cat Breeds<br />Machine Learning</h1>
              </div>
              <div>약 7만장의 이미지 학습을 통한</div>
              <div>러시안블루, 샴, 렉돌, 먼치킨,</div>
              <div>뱅갈, 스핑크스, 페르시안, 아비시니안 등</div>
              <b>48종의 고양이 분류</b>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" sm="4" md="4" lg="3" xl="3">
          <v-card
            class="elevation-0 transparent"
            color="grey lighten-3"
            data-aos="fade-up"
            data-aos-delay="200"
            data-aos-duration="700"
          >
            <v-card-text class="text-center ma-auto">
              <div class="card__title">
                <v-icon x-large class="pb-4">mdi-brain</v-icon>
                <h1 class="headline text-xs-center pb-8">Supervised Learning<br />Classification</h1>
              </div>
              <div><b>CNN 모델 설계</b> (이미지 특징을 추출 특화)</div>
              <div>수집한 품종별 고양이 이미지를 학습한</div>
              <b>지도 학습 기반 분류 모델</b>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" sm="4" md="4" lg="3" xl="3">
          <v-card
            class="elevation-0 transparent"
            color="grey lighten-3"
            data-aos="fade-up"
            data-aos-delay="300"
            data-aos-duration="700"
          >
            <v-card-text class="text-center ma-auto">
              <div class="card__title">
                <v-icon x-large class="pb-4">mdi-trending-up</v-icon>
                <h1 class="headline text-xs-center pb-8">Model Architecting</h1>
              </div>
              <div>옥스포드대학 <b>VGG 모델</b> 참고</div>
              <div><b>Convolution Layer</b>와<br /><b>Pooling Layer</b>를 사용해 특징추출</div>
              <div><b>Dropout Layer</b>를 삽입하여 <b>성능 향상</b></div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" lg="9" xl="9">
          <v-card
            class="elevation-0 transparent"
            color="grey lighten-3"
            data-aos="fade-up"
            data-aos-delay="100"
            data-aos-duration="700"
          >
            <v-card-text class="cardBox__chart">
              <span>
                <v-img class="mainBox__previewImg" contain max-height="360" src="@/assets/img/chart_img.png"></v-img>
              </span>
              <span class="chart__discription">
                <div class="text-h5 mb-5">Performance Improvement</div>
                <div class="text-body-1 mt-4">학습 데이터(이미지)의 해상도 증가, Optimizer 변경,</div>
                <div class="text-body-1">
                  학습 시 Augmentation 이미지 사용,<br />
                  Epoch를 반복 시 이미지 중복을 막기위해 Keras의 ImageGenerator 사용.
                </div>
                <div class="text-body-1 mt-5">
                  <b>지속적인 성능향상 진행</b>
                </div>
              </span>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </section>

    <section id="mainContent">
      <v-parallax dark height="600" src="@/assets/img/cat_bg.jpeg">
        <v-row align="center" class="px-5">
          <v-spacer />
          <v-col cols="12" lg="9" xl="9">
            <div class="content__mainBox">
              <div v-if="loading" class="mainBox__loding">
                <v-img contain max-height="300" src="@/assets/img/loading.gif" />
                <div class="black--text text-center font-weight-bold text-h6">Loading ...</div>
              </div>
              <div v-else-if="modelResult == undefined" class="mainBox__uploadFormBox">
                <v-form ref="uploadForm">
                  <v-file-input
                    v-model="catImgFile"
                    accept="image/*"
                    :rules="rules"
                    placeholder="Upload your Cat Img"
                    label="Cat image file input"
                    prepend-icon="mdi-paperclip"
                    @change="changeUserImgFile"
                  />
                </v-form>

                <v-img v-if="previewImgSrc" class="mainBox__previewImg" contain max-height="300" :src="previewImgSrc" />
                <div v-else class="mainBox__previewImg mainBox__previewImg--noImg">
                  <div class="noImg__discription">
                    <v-icon x-large class="pb-4">mdi-image</v-icon>
                    <div x-class="pb-4">고양이 사진을 등록해 주세요</div>
                  </div>
                </div>

                <div class="mainBox__action">
                  <v-btn class="blue lighten-2 mt-50" dark large @click="clickRunBtn">Run</v-btn>
                </div>
              </div>
              <div v-else class="mainBox__resultBox">
                <div class="mainBox__title">당신의 고양이는 {{ resultCateBreed }} 입니다!</div>
                <v-row>
                  <v-col cols="6">
                    <v-img class="mainBox__previewImg" contain max-height="300" :src="previewImgSrc" />
                  </v-col>
                  <v-col cols="6">
                    <v-img class="mainBox__previewImg" contain max-height="300" :src="catBreedImg" />
                  </v-col>
                </v-row>
                <div class="mainBox__action">
                  <v-btn class="blue lighten-2 mt-50" dark large @click="clearResult">Retry</v-btn>
                </div>
              </div>
            </div>
          </v-col>
          <v-spacer />
        </v-row>
      </v-parallax>
    </section>

    <section>
      <div class="text-h3 text-center font-weight-bold">
        Developers
      </div>
      <div class="content__profileBox" data-aos="fade-up" data-aos-delay="100" data-aos-duration="700">
        <span class="profilBox__card">
          <v-avatar size="200">
            <v-img src="https://avatars.githubusercontent.com/u/5144422?v=4" alt="Avatar" />
          </v-avatar>
          <div class="text-center mt-4">
            <div class="text-subtitle-2 text-center">12184004</div>
            <div class="text-subtitle-1 text-center font-weight-bold ">Gunyoung Yoon</div>
            <div>
              <v-btn color="red" icon large class="ma-5" href="mailto:me@dry8r3ad.com">
                <v-icon>
                  mdi-gmail
                </v-icon>
              </v-btn>
              <v-btn color="black" icon large class="ma-5" target="_blank" href="https://github.com/Dry8r3aD">
                <v-icon>
                  mdi-github
                </v-icon>
              </v-btn>
            </div>
          </div>
        </span>
        <span class="profilBox__card">
          <v-avatar size="200">
            <v-img src="https://avatars.githubusercontent.com/u/61675057?v=4" alt="Avatar" />
          </v-avatar>
          <div class="text-center mt-4">
            <div class="text-subtitle-2 text-center">12184006</div>
            <div class="text-subtitle-1 text-center font-weight-bold">Junhwa Lee</div>
            <div>
              <v-btn color="red" icon large class="ma-5" href="mailto:murisu07@gmail.com">
                <v-icon>
                  mdi-gmail
                </v-icon>
              </v-btn>
              <v-btn
                color="black"
                icon
                large
                class="ma-5"
                target="_blank"
                href="https://github.com/Dry8r3aD/catBreedClassifier"
              >
                <v-icon>
                  mdi-github
                </v-icon>
              </v-btn>
            </div>
          </div>
        </span>
      </div>
    </section>

    <v-footer class="black ma-0 pa-3">
      <v-row wrap align="center">
        <v-col cols="12">
          <div class="white--text ml-3 text-center">
            <v-icon class="white--text mr-1">mdi-school-outline</v-icon>
            2021 AI Class Final Test
          </div>
        </v-col>
      </v-row>
    </v-footer>
  </v-container>
</template>

<script>
import * as modelAPI from "@/api/model.js";

export default {
  name: "Home",

  data: () => ({
    enableCatBreedList: [
      "Abyssinian?",
      "American Bobtail?",
      "American Curl?",
      "American Shorthair?",
      "Applehead Siamese?",
      "Balinese?",
      "Bengal?",
      "Birman?",
      "Bombay?",
      "British Shorthair?",
      "Burmese?",
      "Calico?",
      "Cornish Rex?",
      "Devon Rex?",
      "Dilute Calico?",
      "Dilute Tortoiseshell?",
      "Egyptian Mau?",
      "Exotic Shorthair?",
      "Extra-Toes Cat?",
      "Havana?",
      "Himalayan?",
      "Japanese Bobtail?",
      "Maine Coon?",
      "Manx?",
      "Munchkin?",
      "Nebelung?",
      "Norwegian Forest Cat?",
      "Ocicat?",
      "Oriental Short Hair?",
      "Oriental Tabby?",
      "Persian?",
      "Pixiebob?",
      "Ragamuffin?",
      "Ragdoll?",
      "Russian Blue?",
      "Scottish Fold?",
      "Siamese?",
      "Siberian?",
      "Snowshoe?",
      "Sphynx?",
      "Tabby?",
      "Tiger?",
      "Tonkinese?",
      "Torbie?",
      "Tortoiseshell?",
      "Turkish Angora?",
      "Turkish Van?",
      "Tuxedo?"
    ],
    rules: [value => !value || value.size < 2000000 || "Size should be less than 2 MB!"],

    modelLayerData: undefined,
    userCatImgData: undefined,

    catImgFile: undefined,
    previewImgSrc: "",
    modelResult: undefined,
    loading: false
  }),
  computed: {
    resultCateBreed() {
      let catBreed = "";
      if (this.modelResult && this.modelResult.ans) {
        catBreed = this.enableCatBreedList[this.modelResult.ans].replace("?", "");
      }
      return catBreed;
    },
    catBreedImg() {
      const img_file_name = this.resultCateBreed + ".jpg";

      return require(`../assets/img/catBreed/${img_file_name}`);
    }
  },
  async created() {},
  methods: {
    async changeUserImgFile(image) {
      if (this.catImgFile == undefined) {
        this.previewImgSrc = "";
        return false;
      }

      const reader = new FileReader();
      reader.onload = e => {
        this.previewImgSrc = e.target.result;
      };

      reader.readAsDataURL(image);
    },
    clickRunBtn() {
      this.runModel().then(result => (this.modelResult = result));
    },
    async runModel() {
      if (!this.$refs.uploadForm.validate()) return;
      if (this.catImgFile == undefined) {
        return false;
      }
      this.loading = true;
      const formData = new FormData();
      formData.append("img_file", this.catImgFile);
      let result = await modelAPI.runModel(formData);

      if (result.ok == true) {
        result.prd = result.prd.map(data => data.toFixed(3));
      }
      this.loading = false;
      return result;
    },
    clearResult() {
      this.modelResult = undefined;
      this.catImgFile = undefined;
      this.previewImgSrc = "";
    }
  }
};
</script>

<style lang="scss" scoped src="@/scss/views/Home.scss"></style>
