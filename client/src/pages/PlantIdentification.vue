<template>
  <q-page
    padding
  >
    <div v-if="imageSrc">
      <div
        class="row gutter-sm"
      >
        <div
          class="col-sm-12 col-md-4"
        >
          <captured-image :imageSrc="imageSrc" />
        </div>
        <div
          class="col-sm-12 col-md-8"
        >
          <more-about />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import CapturedImage from '../components/PlantIdentification/CapturedImage';
import MoreAbout from '../components/PlantIdentification/MoreAbout';

export default {
  name: 'PlantIdentification',
  components: {
    CapturedImage,
    MoreAbout,
  },
  props: {
    filePath: {
      type: String,
    },
  },
  data() {
    return {
      imageSrc: '',
      latitude: 0,
      longitude: 0,
    };
  },
  mounted() {
    if (this.filePath) {
      this.uploadAndIdentify(this.filePath);
    }
  },
  methods: {
    uploadAndIdentify(filePath) {
      const view = this;
      // TODO: There's a noticeable delay before the spinner and overlay appears
      view.$q.loading.show({
        delay: 100, // ms
        message: 'Uploading and identifying...',
      });

      const displayErrorMessage = () => {
        view.$q.loading.hide();
        view.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Image upload failed',
          icon: 'report_problem',
        });
      };
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
        const appHost = 'https://7abf2851.ngrok.io';
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
  },
};
</script>

<style>
</style>
