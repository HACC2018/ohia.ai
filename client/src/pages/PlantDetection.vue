<template>
  <q-page class="flex flex-center">
    <q-btn color="primary" label="Get Picture" @click="captureImage" />
    <img :src="imageSrc">
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      imageSrc: '',
    };
  },
  methods: {
    captureImage() {
      navigator.camera.getPicture(
        (data) => { // on success
          this.imageSrc = `data:image/jpeg;base64,${data}`;
        },
        () => { // on fail
          this.$q.notify('Could not access device camera.');
        },
        {
          quality: 75,
        },
      );
    },
  },
};
</script>
