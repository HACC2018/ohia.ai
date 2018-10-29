<template>
  <q-card>
    <q-card-title>
      Plant Detection
    </q-card-title>

    <q-card-main>
      <q-btn color="primary" label="Detect Plant" @click="captureImage" />

      <img :src="imageSrc">
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
      imageSrc: '',
    };
  },
  methods: {
    captureImage() {
      const { camera } = navigator;
      camera.getPicture(
        (data) => { // on success
          this.imageSrc = `data:image/jpeg;base64,${data}`;
        },
        () => { // on fail
          this.$q.notify('Could not access device camera.');
        },
        {
          // Camera options
          // Refer to:
          //   https://cordova.apache.org/docs/en/latest/reference/
          //   cordova-plugin-camera/index.html#cameracameraoptions--object
          quality: 75, // 75% of full image quality
          destinationType: camera.DestinationType.DATA_URL, // Return native uri for iOS
          sourceType: camera.PictureSourceType.CAMERA, // Use camera
          allowEdit: false, // Allow editing of image before selection
          encodingType: camera.EncodingType.JPEG, // Or PNG
          correctOrientation: true, // Allow for correction if device is rotated
          saveToPhotoAlbum: false, // Do not save the image to user Photos
          cameraDirection: camera.Direction.BACK, // Use the back-facing camera
        },
      );
    },
  },
};
</script>
