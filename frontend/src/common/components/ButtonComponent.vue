<template>
  <ion-button :class="className" :id="id" :expand="expand" :shape="shape" :fill="fill" :size="size" :color="color" :style="styleProps">{{ text }}</ion-button>
</template>

<script>
  import { IonButton } from '@ionic/vue';
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'ButtonComponent',
    props: {
      className: String,
      id: String,
      text: String,
      expand: String,
      shape: String,
      fill: String,
      size: String,
      styleProps: String,
      color: String
    },
    components: { IonButton }
  });
</script>