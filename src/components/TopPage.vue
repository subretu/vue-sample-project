<template>
  <section class="home-hero">
    <v-container fluid fill-height class="home-hero__content">
      <v-row>
        <v-col class="home-hero__content-text"> </v-col>
      </v-row>
    </v-container>
  </section>
</template>
<style lang="scss" scoped>
.home-hero__content {
  background: url("../assets/img/text_youkoso.png");
  background-size: cover;
  background-position: center center;
  width: 100%;
  height: 80vh;

  &-text {
    color: white;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
  }
}
</style>
