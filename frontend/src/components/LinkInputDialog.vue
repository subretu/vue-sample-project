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
  ref,
  computed,
  SetupContext,
} from "@vue/composition-api";

export default defineComponent({
  name: "LinkInputDialog",

  props: {
    openStatus: { type: Boolean },
  },

  setup(props, context: SetupContext) {
    interface Data {
      link: { [key: string]: string } | undefined;
    }

    const openStatus2 = computed({
      get: () => props.openStatus,
      set: (value: boolean) => context.emit("OpenStatusRequest", value),
    });

    const data = reactive<Data>({
      link: {},
    });

    const state = reactive({
      inputtext1: "",
      inputtext2: "",
    });

    const show = ref(false);

    const createLink = () => {
      show.value = true;
      const newLink = {
        ...data.link,
        [state.inputtext1]: state.inputtext2,
      };
      data.link = newLink;

      state.inputtext1 = "";
      state.inputtext2 = "";
    };

    return {
      data,
      state,
      show,
      openStatus2,
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
