<template>
  <v-form v-model="valid" ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col xl="12" cols="12">
                <h3 class="mb-2">項目A</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  counter="50"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-divider class="mb-7"></v-divider>
            <v-row>
              <v-col xl="12" cols="12">
                <h3 class="mb-2">項目B</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  counter="50"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-divider class="mb-7"></v-divider>
            <v-row>
              <v-col>
                <v-btn depressed color="info">登録</v-btn>
              </v-col>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "InputText",
});
</script>

<style>
.input-text {
  width: 700px;
}
</style>
