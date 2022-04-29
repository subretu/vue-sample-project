<template>
  <v-app>
    <v-app-bar color="primary" dark app clipped-left>
      <template>
        <v-tabs>
          <v-tab to="/userlist">USERLIST</v-tab>
          <v-tab>Item Two</v-tab>
          <v-tab>Item Three</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: null,
      supports: [
        {
          name: "Consulting and suppourt",
          icon: "mdi-vuetify",
          link: "/consulting-and-support",
        },
        {
          name: "Discord community",
          icon: "mdi-discord",
          link: "/discord-community",
        },
        {
          name: "Report a bug",
          icon: "mdi-bug",
          link: "/report-a-bug",
        },
        {
          name: "Github issue board",
          icon: "mdi-github",
          link: "/guthub-issue-board",
        },
        {
          name: "Stack overview",
          icon: "mdi-stack-overflow",
          link: "/stack-overview",
        },
      ],
      nav_lists: [
        {
          name: "Getting Started",
          icon: "mdi-speedometer",
          lists: ["Quick Start", "Pre-made layouts"],
        },
        {
          name: "Customization",
          icon: "mdi-cogs",
        },
        {
          name: "Styles & animations",
          icon: "mdi-palette",
          lists: ["Colors", "Content", "Display"],
        },
        {
          name: "UI Components",
          icon: "mdi-view-dashboard",
          lists: ["API explorer", "Alerts"],
        },
        {
          name: "Directives",
          icon: "mdi-function",
        },
        {
          name: "Preminum themes",
          icon: "mdi-vuetify",
        },
      ],
    };
  },
};
</script>
