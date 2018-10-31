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
      const { camera } = navigator;
      camera.getPicture(
        (filePath) => {
          const view = this;
          window.requestFileSystem(LocalFileSystem.PERSISTENT, 0, function (fs) {
            console.log('File system open:', fs.name);
            window.resolveLocalFileSystemURL(filePath, function(fileEntry) {
              fileEntry.file(function(file) {
                const reader = new FileReader();
                reader.onloadend = function(event) {
                  console.log('Image byte length:', event.target.result.byteLength);
                  // Create a blob based on the FileReader "result",
                  // which we asked to be retrieved as an ArrayBuffer
                  const arrayBufferView = new Uint8Array(this.result);
                  const blob = new Blob([arrayBufferView], { type: 'image/jpeg' });
                  const formData = new FormData();
                  formData.append('image.latitude', view.latitude);
                  formData.append('image.longitude', view.longitude);
                  formData.append('image', blob);

                  const appHost = 'http://localhost:3000';
                  const imageUploadUrl = `${appHost}/images/upload`;
                  view.$axios.post(imageUploadUrl, formData)
                    .then((res) => {
                      view.testing = res.data.success;
                    })
                    .catch(() => {
                      view.$q.notify({
                        color: 'negative',
                        position: 'top',
                        message: 'Image upload failed',
                        icon: 'report_problem',
                      });
                    });
                };
                console.log('Reading file:', file.name);
                // Read the file as an ArrayBuffer
                reader.readAsArrayBuffer(file);
              }, function(err) {
                console.error('Error getting fileEntry file:', err);
              });
            }, function(err) {
              console.error('Error resolving the local file system URL:', err);
            });
          }, function(err) {
            console.error('Error getting persistent fs:', err);
          });
        },
        () => {
          this.$q.notify('Could not access device camera.');
        },
        {
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
        },
      );
    },
  },
};
</script>
