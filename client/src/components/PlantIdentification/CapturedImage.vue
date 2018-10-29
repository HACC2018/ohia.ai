<template>
  <q-card>
    <q-card-title>
      Plant Identification
    </q-card-title>

    <q-card-media>
      <img src="https://www.hawaiimagazine.com/sites/default/files/field/image/25040492391_b5f4f063c2_k.jpg">

    </q-card-media>

    <q-card-main>Classify the following plant:</q-card-main>

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
      float-label="Self-Identify"
    />

    <br />

  </q-card>
</template>

<script>
export default {
  data() {
    return {
      type: '',
      selfIdentify: '',
    };
  },
};
</script>

<style>

</style>
