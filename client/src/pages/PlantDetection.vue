<template>
  <q-card>
    <q-card-title>
      Plant Detection
    </q-card-title>

    <q-card-main>
      <q-btn color="primary" label="Detect Plant" @click="captureImage" />

      <img :src="imageSrc">
      {{ testing }}
    </q-card-main>
  </q-card>
</template>

<style>
</style>

<script>
export default {
  name: 'PlantDetection',
  data() {
    return {
      testing: 'start',
      imageSrc: '',
    };
  },
  methods: {
    captureImage() {
      // const imageData = new FormData();
      const payload = {
        // uri: filePath,
        // name: 'test_photo.jpg',
        // type: 'image/jpg',
        sample: 'payload',
      };
      // imageData.append('json', JSON.stringify(payload));

      const url = 'https://big-vampirebat-16.localtunnel.me/images/upload';
      this.$axios.post(url, payload)
        .then((res) => {
          this.testing = res.data.success;
        })
        .catch(() => {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Image upload failed',
            icon: 'report_problem',
          });
        });
    },
  },
};
</script>
