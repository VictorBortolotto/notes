<style>
  @import './styles/home.style.css';
</style>

<template>
  <div class="notes-container" id="main-content">
    <HeaderComponent style="--background: rgb(93, 221, 93);">
      <ButtonComponent styleProps="display: flex; align-items: center; justify-content: center; width: 5%; height: 30px; color: white; --background: rgb(93, 221, 93); margin-left: 1%;">
          <ion-menu-button style="color: white; width: 100%; height: 100%"></ion-menu-button>
      </ButtonComponent>
    </HeaderComponent>
    <CardComponent styleProps="width: 98%; height: 80%; --background: white;">
      <CardContentComponent styleProps="display: flex; align-itens: center; justify-content: center; margin: 0px; padding: 0 0 0 0">
        <GridComponent>
          <GridRowComponent>
            <GridColumnComponent v-for="(item, index) in getTestList()" :key="index" size="4">
              <CardComponent>
                <CardHeaderComponent styleProps="--background: white; min-height: 150px;">
                  <CardTitleTextComponent>
                    {{ item.name  }}
                  </CardTitleTextComponent>
                </CardHeaderComponent>
              </CardComponent>
            </GridColumnComponent>
          </GridRowComponent>
        </GridComponent>
      </CardContentComponent>
    </CardComponent>
    <NewTaskModalComponent></NewTaskModalComponent>
    <SidebarMenuComponent></SidebarMenuComponent>
    <FloatActionButton id="open-dialog"></FloatActionButton>
  </div>
</template>

<script setup>
  import HeaderComponent from '../../common/components/headerComponent/HeaderComponent.vue';
  import ButtonComponent from '../../common/components/buttomComponent/ButtonComponent.vue';
  import SidebarMenuComponent from '../../common/components/sideBarComponent/SidebarMenuComponent.vue';
  import CardComponent from '../../common/components/cardComponent/CardComponent.vue';
  import CardContentComponent from '../../common/components/cardComponent/CardContentComponent.vue';
  import CardHeaderComponent from '../../common/components/cardComponent/CardHeaderComponent.vue';
  import CardTitleTextComponent from '../../common/components/cardComponent/CardTitleTextComponent.vue';
  import FloatActionButton from '../../common/components/floatActionButton/FloatActionButton.vue';
  import GridComponent from '../../common/components/gridComponent/GridComponent.vue';
  import GridRowComponent from '../../common/components/gridComponent/GridRowComponent.vue';
  import GridColumnComponent from '../../common/components/gridComponent/GridColumnComponent.vue';
  import NewTaskModalComponent from './components/NewTaskModalComponent.vue';
  import { IonMenuButton } from '@ionic/vue';
  import { getTestList } from './js/NotesList.js' 
</script>./js/NotesList.js