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
        :thumbnails="images"
        thumbnails-horizontal
      >
        <q-carousel-slide
          v-for="(image, i) in images"
          :img-src="image"
          :key="i"
        />

        <q-carousel-control
          slot="control-button"
          slot-scope="carousel"
          position="bottom-right"
          :offset="[18, 22]"
        >
          <q-btn
            round dense push
            color="primary"
            :icon="carousel.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
            @click="carousel.toggleFullscreen()"
          />
        </q-carousel-control>
      </q-carousel>
    </q-card-main>
  </q-card>
</template>

<script>
export default {
  props: {
    id: {
      type: String,
    },
  },
  data() {
    return {
      images: [],
    };
  },
  mounted() {
    this.$axios
      .get(`http://localhost:3000/api/images/${this.id}`)
      .then((response) => {
        const { data } = response;
        console.log(data);
        // eslint-ignore-next-line
        this.images = data.map(image => image.image_url);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>

</style>
