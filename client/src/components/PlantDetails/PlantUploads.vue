<template>
  <q-card>
    <q-card-title>
      Uploads
    </q-card-title>

    <q-card-separator />

    <q-card-main>
      <q-carousel
        color="white"
        arrows
        height="300px"
        :thumbnails="[
          'https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg',
          'https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg',
          'https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg',
          'https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg',
        ]"
        thumbnails-horizontal
      >
        <q-carousel-slide img-src="https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg" />
        <q-carousel-slide img-src="https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg" />
        <q-carousel-slide img-src="https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg" />
        <q-carousel-slide img-src="https://wildlifeofhawaii.com/images/flowers/Metrosideros-polymorpha-1.jpg" />
      </q-carousel>
    </q-card-main>
  </q-card>
</template>

<script>
export default {

};
</script>

<style>

</style>
