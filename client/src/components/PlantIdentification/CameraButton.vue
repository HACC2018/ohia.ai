<template>
  <q-btn v-bind="button" @click="captureImage">{{ text }}</q-btn>
</template>

<script>
export default {
  name: 'CameraButton',
  props: {
    text: {
      type: String,
    },
    button: {
      type: Object,
    },
  },
  methods: {
    captureImage() {
      const view = this;
      const { camera } = navigator;
      const cameraOptions = {
        // Camera options
        // Refer to:
        //   https://cordova.apache.org/docs/en/latest/reference/
        //   cordova-plugin-camera/index.html#cameracameraoptions--object
        quality: 50, // 50% of full image quality
        destinationType: camera.DestinationType.NATIVE_URI, // Return native uri for iOS
        sourceType: camera.PictureSourceType.CAMERA, // Use camera
        allowEdit: false, // Allow editing of image before selection
        encodingType: camera.EncodingType.JPEG, // Or PNG
        correctOrientation: true, // Allow for correction if device is rotated
        saveToPhotoAlbum: false, // Do not save the image to user Photos
        cameraDirection: camera.Direction.BACK, // Use the back-facing camera
      };

      camera.getPicture(
        (filePath) => {
          view.$router.push({
            name: 'identify',
            params: { filePath },
          });
        },
        (err) => {
          console.error('Error accessing the device camera:', err);
          view.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Could not access device camera',
            icon: 'report_problem',
          });
        },
        cameraOptions,
      );
    },
  },
};
</script>

<style>
</style>
