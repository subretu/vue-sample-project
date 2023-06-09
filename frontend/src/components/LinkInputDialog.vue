<template>
  <v-form>
    <v-container>
      <v-dialog v-model="dialogOpenStatus" width="auto">
        <v-card>
          <v-card-title />
          <v-row>
            <v-col>
              <h3 class="mb-2 ml-3" align="left">タイトル</h3>
              <v-text-field
                label="タイトルを入力してください"
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
                label="URLを入力してください"
                placeholder="https://"
                outlined
                dense
                class="input-text ml-3 mr-3"
                v-model="state.inputtext2"
                @input="emitInput"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-card-actions>
            <v-btn
              color="info"
              depressed
              align="right"
              @click="createLink"
              :disabled="!mytext"
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
  watch,
} from "@vue/composition-api";

export default defineComponent({
  name: "LinkInputDialog",

  props: {
    openStatus: { type: Boolean },
  },

  setup(props, context: SetupContext) {
    const dialogOpenStatus = computed({
      get: () => props.openStatus,
      set: (value: boolean) => context.emit("OpenStatusRequest", value),
    });

    const state = reactive({
      inputtext1: "",
      inputtext2: "",
    });

    const emitInput = () => {
      context.emit("input", state);
    };

    const createLink = () => {
      context.emit("displayLink");
      state.inputtext1 = "";
      state.inputtext2 = "";
    };

    // 両方に入力があればボタンをクリック可能
    const mytext = computed(() => {
      return state.inputtext1 && state.inputtext2;
    });

    watch(
      () => dialogOpenStatus.value,
      (openStatus) => {
        if (openStatus) {
          state.inputtext1 = "";
          state.inputtext2 = "";
        }
      }
    );

    return {
      state,
      dialogOpenStatus,
      emitInput,
      createLink,
      mytext,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 800px;
}
</style>
