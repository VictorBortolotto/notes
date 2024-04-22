<style>
  @import '../styles/notes.style.css';
</style>

<template>
  <div class="notes-container" id="main-content">
    <HeaderComponent style="--background: rgb(93, 221, 93);">
      <ButtonComponent styleProps="display: flex; align-items: center; justify-content: center; width: 5%; height: 30px; color: white; --background: rgb(93, 221, 93); margin-left: 1%;">
          <ion-menu-button style="color: white; width: 100%; height: 100%"></ion-menu-button>
      </ButtonComponent>
    </HeaderComponent>
    <SidebarMenuComponent></SidebarMenuComponent> 
    <FloatActionButton></FloatActionButton>
  </div>
</template>

<script setup>
  import HeaderComponent from '../common/components/headerComponent/HeaderComponent.vue';
  import ButtonComponent from '../common/components/buttomComponent/ButtonComponent.vue';
  import SidebarMenuComponent from '../common/components/sideBarComponent/SidebarMenuComponent.vue';
  import FloatActionButton from '../common/components/floatActionButton/FloatActionButton.vue';
  import { IonMenuButton } from '@ionic/vue';
</script>