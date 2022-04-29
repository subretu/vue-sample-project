<template>
  <v-app>
    <v-app-bar color="primary" dark app clipped-left>
      <template>
        <v-tabs>
          <v-tab to="/userlist">USERLIST</v-tab>
          <v-tab to="/tasklist">TASKLIST</v-tab>
          <v-tab to="/axiostest">AXIOSTEST</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
