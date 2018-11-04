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
          <captured-image
            :imageId="imageId"
            :imageSrc="imageSrc"
            :predictions="predictions"
          />
        </div>
        <div
          class="col-sm-12 col-md-8"
        >
          <more-about :predictions="predictions" />
        </div>
      </div>
    </div>
    <div v-else align="center" class="absolute-center loading-block">
      <q-spinner color="primary" :size="84" />
      <div class="loading-text">
        <q-title padding>Uploading and identifying...</q-title>
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
    latitude: {
      type: Number,
    },
    longitude: {
      type: Number,
    },
  },
  data() {
    return {
      imageId: 0,
      imageSrc: '',
      predictions: [],
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
      const CANDIDATE_COLORS = ['green', 'orange', 'red'];

      const displayErrorMessage = () => {
        view.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Image upload failed',
          icon: 'report_problem',
        });
        view.$router.push({
          path: '/',
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
        const latitude = typeof view.latitude === 'number' ? view.latitude : null;
        const longitude = typeof view.longitude === 'number' ? view.longitude : null;
        formData.append('latitude', latitude);
        formData.append('longitude', longitude);
        formData.append('image', blob);
        return formData;
      };
      function uploadImage() {
        const blob = convertImageToBlob(this.result);
        const formData = constructFormData(blob);
        const url = `${process.env.API_HOST}/images/upload`;
        view.$axios.post(url, formData)
          .then((res) => {
            console.log('res.data', JSON.stringify(res.data.predictions));
            const fullPath = filePath
              .replace('assets-library://', 'cdvfile://localhost/assets-library/');
            view.imageId = res.data.id;
            view.imageSrc = fullPath;
            view.predictions = res.data.predictions.map((pred, index) => ({
              ...pred,
              color: CANDIDATE_COLORS[index],
            }));
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
.loading-block {
  width: 260px;
}
.loading-text {
  margin-top: 32px;
}
</style>
