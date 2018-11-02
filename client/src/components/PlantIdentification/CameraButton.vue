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
  data() {
    return {
      imageSrc: '',
      latitude: 0,
      longitude: 0,
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
        view.$q.loading.hide();
        view.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Image upload failed',
          icon: 'report_problem',
        });
      };

      camera.getPicture(
        (filePath) => {
          // TODO: There's a noticeable delay before the spinner and overlay appears
          view.$q.loading.show({
            delay: 100, // ms
            message: 'Uploading and identifying...',
          });
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
            const appHost = 'https://78d4349c.ngrok.io';
            const imageUploadUrl = `${appHost}/images/upload`;
            view.$axios.post(imageUploadUrl, formData)
              .then((res) => {
                console.log('res.data', JSON.stringify(res.data.predictions));
                view.$q.loading.hide();
                const fullPath = filePath
                  .replace('assets-library://', 'cdvfile://localhost/assets-library/');
                view.imageSrc = fullPath;
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
          view.$q.loading.hide();
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
