<script type="text/javascript" charset="utf-8">
      webix.ready(function () {
        gridA = webix.ui({
          id: "qbcudpyz",
          container: "webix_datatable",
          select: "row",
          view: "datatable",
          columns: [
            {
              id: "name",
              header: {
                text: "Project",
              },
              sort: "string",
              width: 200,
              hidden: 0,
            },
          ],
          minHeight: 100,
          autoheight: true,
          on: {
            onBeforeLoad: function () {
              this.showOverlay("Loading...");
            },
            onAfterLoad: function () {
              if (!this.count()) this.showOverlay("Sorry, there is no data");
              else this.hideOverlay();
            },
          },
          url: function () {
            return webix.promise(function (res) {
              setTimeout(function () {
                res(webix.ajax(url));
              }, 1000);
            });
          },
        })
      });
</script>