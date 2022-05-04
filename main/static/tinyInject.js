var s = document.createElement("script");
s.type = "text/javascript";
s.src =
  "https://cdn.tiny.cloud/1/jwf99p872r5uy8rojznr04o1rf1b7d415r2wy6n2mkhhrr84/tinymce/5/tinymce.min.js";
document.head.appendChild(s);
s.onload = function () {
  var editor = tinymce.init({
    selector: "textarea:first",
    plugins:
      "print code preview codesample paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars emoticons",
    imagetools_cors_hosts: ["picsum.photos"],
    menubar: "file edit view codesample insert format tools table help",
    toolbar:
      "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl",
    toolbar_sticky: true,
    autosave_ask_before_unload: true,
    autosave_interval: "30s",
    autosave_prefix: "{path}{query}-{id}-",
    autosave_restore_when_empty: false,
    autosave_retention: "2m",
    image_advtab: true,
    images_upload_url: "/upload_image/",
    document_base_url: "https://www.codersarea.com",
    // document_base_url: 'http://localhost:8000',

    // relative_urls: false,
    convert_urls: false,
    remove_script_host: false,
    automatic_uploads: true,
    images_reuse_filename: true,
    content_css: "//www.tiny.cloud/css/codepen.min.css",
    link_list: [
      { title: "My page 1", value: "http://www.tinymce.com" },
      { title: "My page 2", value: "http://www.moxiecode.com" },
    ],
    image_list: [
      { title: "My page 1", value: "http://www.tinymce.com" },
      { title: "My page 2", value: "http://www.moxiecode.com" },
    ],
    image_class_list: [
      { title: "None", value: "" },
      { title: "Some class", value: "class-name" },
    ],
    importcss_append: true,
    file_picker_callback: function (callback, value, meta) {
      /* Provide file and text for the link dialog */
      if (meta.filetype === "file") {
        callback("https://www.google.com/logos/google.jpg", {
          text: "My text",
        });
      }

      /* Provide image and alt text for the image dialog */
      if (meta.filetype === "image") {
        callback("https://www.google.com/logos/google.jpg", {
          alt: "My alt text",
        });
      }

      /* Provide alternative source and posted for the media dialog */
      if (meta.filetype === "media") {
        callback("movie.mp4", {
          source2: "alt.ogg",
          poster: "https://www.google.com/logos/google.jpg",
        });
      }
    },
    templates: [
      {
        title: "New Table",
        description: "creates a new table",
        content:
          '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>',
      },
      {
        title: "Starting my story",
        description: "A cure for writers block",
        content: "Once upon a time...",
      },
      {
        title: "New list with dates",
        description: "New List with dates",
        content:
          '<div class="mceTmpl"><span class="cdate">cdate</span><br /><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>',
      },
    ],
    template_cdate_format: "[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]",
    template_mdate_format: "[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]",
    height: 800,
    image_caption: true,
    quickbars_selection_toolbar:
      "bold italic | quicklink h2 h3 blockquote quickimage quicktable",
    noneditable_noneditable_class: "mceNonEditable",
    toolbar_mode: "sliding",
    contextmenu: "link image imagetools table",
    setup: function (ed) {
      ed.on("KeyDown", function (e) {
        if ((e.keyCode == 8 || e.keyCode == 46) && ed.selection) {
          // delete & backspace keys

          var selectedNode = ed.selection.getNode(); // get the selected node (element) in the editor
          console.log("delete key is pressed");
          if (selectedNode && selectedNode.nodeName == "IMG") {
            deleteImage(selectedNode.src); // A callback that will let me invoke the deletion of the image on the server if appropriate for the image source.
          }
        } else {
          console.log("another key is pressed");
        }
      });
    },
  });
};

function deleteImage(url) {
  fetch("/delete_image/", {
    method: "POST",
    body: "url=" + url,
    headers: {
      "Content-type": "application/x-www-form-urlencoded",
    },
  }).then(
    (response) => {
      console.log("done.......");
      alert("Deleted..");
    },
    (error) => {
      console.log("error.........");
      alert("Not Deleted..");
    }
  );
}
