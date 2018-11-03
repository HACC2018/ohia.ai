<template>
  <q-card>
    <q-card-title>
      Plant Identification Results
    </q-card-title>

    <q-card-separator />
    <div class="image-background">
      <img :src="imageSrc" class="image" />
    </div>
    <q-card-separator />

    <q-card-main>Classify the plant above:</q-card-main>
    <q-card-separator />

    <q-card-actions align="center">
      <template v-for="pred in predictions">
        <q-btn
          v-bind:key="pred.id"
          flat
          :color="pred.color"
          @click="classifyPlant"
        >
          {{ pred.className }}
        </q-btn>
      </template>
      <q-btn @click="classifyPlant" flat>I don't know</q-btn>
    </q-card-actions>

    <q-card-separator />

    <q-input
      class="q-ma-md"
      v-model="selfIdentify"
      float-label="Enter the plant name if you know it"
    />

    <br />

  </q-card>
</template>

<script>
export default {
  name: 'CapturedImage',
  props: {
    imageSrc: {
      type: String,
    },
    predictions: {
      type: Array,
    },
  },
  data() {
    return {
      selfIdentify: '',
    };
  },
  methods: {
    classifyPlant() {
      // TODO
    },
  },
};
</script>

<style>
.image-background {
  background: #E6E6E6;
}
.image {
  width: auto;
  height: 270px;
  display: block;
  margin: 0 auto;
}
</style>
