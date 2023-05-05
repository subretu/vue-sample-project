<template>
  <v-app>
    <v-app-bar color="primary" dark app clipped-left>
      <template>
        <v-tabs>
          <v-tab to="/userlist">USERLIST</v-tab>
          <v-tab to="/userlist2">USERLIST2</v-tab>
          <v-tab to="/tasklist">TASKLIST</v-tab>
          <v-tab to="/tasklist2">TASKLIST2</v-tab>
          <v-tab to="/axiostest">AXIOSTEST</v-tab>
          <v-tab to="/chartsample">CHARTSAMPLE</v-tab>
          <v-tab to="/fileupload">FILEUPLOAD</v-tab>
          <v-tab to="/fileupload2">FILEUPLOAD2</v-tab>
          <v-tab to="/Inputtext">INPUTTEXT</v-tab>
          <v-tab to="/createlink">CREATELINK</v-tab>
          <v-tab to="/dbvaluesdisplay">DBVALUEDISPLAY</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
