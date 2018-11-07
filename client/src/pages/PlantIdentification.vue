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
          <more-about
            :imageId="imageId"
            :imageSrc="imageSrc"
            :predictions="predictions"
          />
        </div>
      </div>
    </div>
    <div v-else align="center" class="absolute-center loading-block">
      <q-spinner color="primary" :size="84" />
      <div class="loading-text">
        <q-card-title padding>Uploading and identifying...</q-card-title>
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
    imageIdProp: {
      type: Number,
    },
    imageSrcProp: {
      type: String,
    },
    predictionsProp: {
      type: Array,
    },
  },
  data() {
    return {
      imageId: this.imageIdProp ? this.imageIdProp : 0,
      imageSrc: this.imageSrcProp ? this.imageSrcProp : '',
      predictions: this.predictionsProp ? this.predictionsProp : [],
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

        function dataURItoBlob(dataURI) {
          // convert base64 to raw binary data held in a string
          // doesn't handle URLEncoded DataURIs - see SO answer #6850276 for code that does this
          var byteString = atob(dataURI.split(',')[1]);

          // write the bytes of the string to an ArrayBuffer
          var ab = new ArrayBuffer(byteString.length);

          // create a view into the buffer
          var ia = new Uint8Array(ab);

          // set the bytes of the buffer to the correct values
          for (var i = 0; i < byteString.length; i++) {
              ia[i] = byteString.charCodeAt(i);
          }

          // write the ArrayBuffer to a blob, and you're done
          var blob = new Blob([ab], {type: 'image/jpg'});
          return blob;

        }
            
        // initialize canvas
        let img = document.createElement("img");
        img.src = result.target.result;
        let canvas = document.createElement("canvas");
        let ctx = canvas.getContext("2d");

        // resize smaller dimension
        const SIZE = 224;
        let width = img.width;
        let height = img.height;        
        if (height > width) {
            if (width > SIZE) {
                height *= SIZE / width;
                width = SIZE;
            }
        } else {
            if (height > SIZE) {
                width *= SIZE / height;
                height = SIZE;
            }
        }
        
        // resize canvas
        canvas.width = width;
        canvas.height = height;
        

        ctx.drawImage(img, 0, 0, width, height);
        
        // convert canvas to DataURL to then to Blob
        const dataurl = canvas.toDataURL("image/jpg");
        document.getElementById('output').src = dataurl;
        
        const blob = dataURItoBlob(dataurl);
        console.log(blob, width, height);
                
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
          reader.readAsDataURL(file);
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
