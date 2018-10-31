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
      latitude: 10,
      longitude: 12,
    };
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
      const displayErrorMessage = () => {
        view.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Image upload failed',
          icon: 'report_problem',
        });
      };

      camera.getPicture(
        (filePath) => {
          const fullPath = filePath.replace('assets-library://', 'cdvfile://localhost/assets-library/');
          view.imageSrc = fullPath;
          const convertImageToBlob = (result) => {
            // Create a blob based on the FileReader "result",
            // which we asked to be retrieved as an ArrayBuffer
            const arrayBufferView = new Uint8Array(result);
            return new Blob([arrayBufferView], { type: 'image/jpeg' });
          };
          const constructFormData = (blob) => {
            const formData = new FormData();
            formData.append('latitude', view.latitude);
            formData.append('longitude', view.longitude);
            formData.append('image', blob);
            return formData;
          };
          function uploadImage() {
            const blob = convertImageToBlob(this.result);
            const formData = constructFormData(blob);
            const appHost = 'https://8e7ef90d.ngrok.io';
            const imageUploadUrl = `${appHost}/images/upload`;
            view.$axios.post(imageUploadUrl, formData)
              .then((res) => {
                view.testing = res.data.success;
              })
              .catch(() => {
                displayErrorMessage();
              });
          }
          window.resolveLocalFileSystemURL(filePath, (fileEntry) => {
            fileEntry.file((file) => {
              const reader = new FileReader();
              reader.onloadend = uploadImage;
              // Read the file as an ArrayBuffer
              reader.readAsArrayBuffer(file);
            }, (err) => {
              console.error('Error retrieving the fileEntry file:', err);
              displayErrorMessage();
            });
          }, (err) => {
            console.error('Error resolving the local file system URL:', err);
            displayErrorMessage();
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
