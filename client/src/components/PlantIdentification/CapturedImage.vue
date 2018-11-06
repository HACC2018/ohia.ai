<template>
  <div>
    <q-card>
      <q-card-title>
        Plant Identification Results
      </q-card-title>

      <q-card-separator />

      <div class="image-background">
        <img :src="imageSrc" class="image" />
      </div>

      <q-card-separator />

      <q-card-main>
        Classify the plant above:
      </q-card-main>

      <q-card-separator />

      <q-card-actions align="center">
        <template v-for="pred in predictions">
          <q-btn
            v-bind:key="pred.id"
            flat
            :color="pred.color"
            @click="classifyPlant(pred.id, null)"
          >
            {{ pred.className }}
          </q-btn>
        </template>
        <q-btn
          @click="classifyPlant(null, null)"
          flat
        >
          I don't know
        </q-btn>
      </q-card-actions>

      <q-card-separator />

      <div class="guess-block">
        <q-input
          class="q-ma-md"
          v-model="userGuess"
          float-label="Or enter the plant name if you know it"
        />
        <div align="right" class="guess-submit">
          <q-btn
            flat
            color="secondary"
            @click="classifyPlant(null, userGuess)"
          >
            Submit Name
          </q-btn>
        </div>
      </div>
    </q-card>

    <q-modal
      v-model="opened"
      align="center"
      minimized
      no-esc-dismiss
      no-backdrop-dismiss
    >
      <div class="modal-block">
        <q-card-title>
          Classification complete!
        </q-card-title>

        <q-icon
          name="spa"
          size="36px"
          color="secondary"
        />

        <p class="text">
          Mahalo for helping to identify the flora of Hawaiʻi.
        </p>

        <q-btn
          flat
          color="secondary"
          label="Close"
          @click="opened = false"
          to="/"
        />
      </div>
    </q-modal>
  </div>
</template>

<script>
export default {
  name: 'CapturedImage',
  props: {
    imageId: {
      type: Number,
    },
    imageSrc: {
      type: String,
    },
    predictions: {
      type: Array,
    },
  },
  data() {
    return {
      opened: false,
      userGuess: '',
    };
  },
  methods: {
    classifyPlant(plantId, userGuess) {
      const url = `${process.env.API_HOST}/api/plant-image/${this.imageId}`;
      this.$axios.put(url, {
        plant_id: plantId,
        identified: !!plantId,
        user_guess: userGuess,
      })
        .then(() => {
          this.opened = true;
        })
        .catch((err) => {
          console.error('Error updating plant image data:', err);
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Classifying plant failed',
            icon: 'report_problem',
          });
        });
    },
  },
};
</script>

<style>
.guess-block {
  padding-bottom: 10px;
}
.guess-submit {
  padding-right: 16px;
}
.image-background {
  background: #E6E6E6;
}
.image {
  width: auto;
  height: 270px;
  display: block;
  margin: 0 auto;
}
.modal-block {
  padding: 10px 24px 20px;
}
.text {
  margin-top: 24px;
}
</style>
