<template>
  <v-app-bar app color="white" flat>
    <div class="d-flex align-center">
      <v-img class="shrink mr-2" contain src="@/assets/logo.png" transition="scale-transition" width="40" />
      <b>Cat Breed Classifier</b>
    </div>
    <v-spacer></v-spacer>
  </v-app-bar>
</template>

<script>
export default {
  name: "AppBar",

  data: () => ({})
};
</script>
