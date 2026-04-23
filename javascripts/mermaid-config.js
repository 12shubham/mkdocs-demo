/*
  Mermaid global configuration with brand colours.

  document$ is Material for MkDocs' RxJS observable — it fires on every
  page load, including instant-navigation transitions, so diagrams
  re-render correctly without a full page refresh.
*/
document$.subscribe(function () {
  /* Re-initialise with brand palette before Material triggers mermaid.run() */
  mermaid.initialize({
    startOnLoad: false,
    theme: "base",
    themeVariables: {
      /* Core orange */
      primaryColor:         "#FD5108",
      primaryTextColor:     "#ffffff",
      primaryBorderColor:   "#FD5108",
      /* Orange 400 for edges */
      lineColor:            "#FE7C39",
      /* Orange 50 for cluster backgrounds */
      secondaryColor:       "#FFF5ED",
      tertiaryColor:        "#FFCDA8",
      background:           "#ffffff",
      mainBkg:              "#FD5108",
      clusterBkg:           "#FFF5ED",
      titleColor:           "#FD5108",
      edgeLabelBackground:  "#FFF5ED",
      fontFamily:           "Inter, sans-serif",
      fontSize:             "14px",
    },
  });
});
