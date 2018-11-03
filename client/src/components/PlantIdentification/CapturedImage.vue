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
      <q-btn flat color="orange">Metrosideros Polymorpha</q-btn>
      <q-btn flat color="red">Acacia Koa</q-btn>
      <q-btn flat color="purple">Musa x paradisiaca</q-btn>
      <q-btn flat>I don't know</q-btn>
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
  },
  data() {
    return {
      type: '',
      selfIdentify: '',
    };
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
