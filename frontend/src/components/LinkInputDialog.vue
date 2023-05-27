<template>
  <v-form>
    <v-container>
      <v-dialog v-model="openStatus2" width="auto">
        <v-card>
          <v-card-title />
          <v-row>
            <v-col>
              <h3 class="mb-2 ml-3" align="left">タイトル</h3>
              <v-text-field
                label="入力してください。"
                outlined
                dense
                class="input-text ml-3 mr-3"
                v-model="state.inputtext1"
                @input="emitInput"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <h3 class="mb-2 ml-3" align="left">URL</h3>
              <v-text-field
                label="入力してください。"
                outlined
                dense
                class="input-text ml-3 mr-3"
                v-model="state.inputtext2"
                @input="emitInput2"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-card-actions>
            <v-btn color="info" depressed align="right" @click="createLink"
              >作成</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import {
  defineComponent,
  reactive,
  computed,
  SetupContext,
} from "@vue/composition-api";

export default defineComponent({
  name: "LinkInputDialog",

  props: {
    openStatus: { type: Boolean },
  },

  setup(props, context: SetupContext) {
    const openStatus2 = computed({
      get: () => props.openStatus,
      set: (value: boolean) => context.emit("OpenStatusRequest", value),
    });

    const state = reactive({
      inputtext1: "",
      inputtext2: "",
    });

    const emitInput = () => {
      context.emit("input1", state.inputtext1);
    };

    const emitInput2 = () => {
      context.emit("input2", state.inputtext2);
    };

    const createLink = () => {
      context.emit("parentFunction");
      state.inputtext1 = "";
      state.inputtext2 = "";
    };

    return {
      state,
      openStatus2,
      emitInput,
      emitInput2,
      createLink,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 800px;
}
</style>
