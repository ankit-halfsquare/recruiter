$(function() {
    "use strict";
    $(function() { $(".preloader").fadeOut() }), jQuery(document).on("click", ".mega-dropdown", function(i) { i.stopPropagation() });
    var i = function() {
        var i = window.innerWidth > 0 ? window.innerWidth : this.screen.width,
            e = 70;
        1170 > i ? ($("body").addClass("mini-sidebar"), $(".navbar-brand span").hide(), $(".scroll-sidebar, .slimScrollDiv").css("overflow-x", "visible").parent().css("overflow", "visible"), $(".sidebartoggler i").addClass("ti-menu")) : ($("body").removeClass("mini-sidebar"), $(".navbar-brand span").show());
        var o = (window.innerHeight > 0 ? window.innerHeight : this.screen.height) - 1;
        o -= e, 1 > o && (o = 1), o > e && $(".page-wrapper").css("min-height", o + "px")
    };
    $(window).ready(i), $(window).on("resize", i), $(".sidebartoggler").on("click", function() { $("body").hasClass("mini-sidebar") ? ($("body").trigger("resize"), $(".scroll-sidebar, .slimScrollDiv").css("overflow", "hidden").parent().css("overflow", "visible"), $("body").removeClass("mini-sidebar"), $(".navbar-brand span").show()) : ($("body").trigger("resize"), $(".scroll-sidebar, .slimScrollDiv").css("overflow-x", "visible").parent().css("overflow", "visible"), $("body").addClass("mini-sidebar"), $(".navbar-brand span").hide()) }), $(".fix-header .topbar").stick_in_parent({}), $(".nav-toggler").click(function() { $("body").toggleClass("show-sidebar"), $(".nav-toggler i").toggleClass("ti-menu"), $(".nav-toggler i").addClass("ti-close") }), $(".sidebartoggler").on("click", function() {}), $(".search-box a, .search-box .app-search .srh-btn").on("click", function() { $(".app-search").toggle(200) }), $(".right-side-toggle").click(function() { $(".right-sidebar").slideDown(50), $(".right-sidebar").toggleClass("shw-rside") }), $(".floating-labels .form-control").on("focus blur", function(i) { $(this).parents(".form-group").toggleClass("focused", "focus" === i.type || this.value.length > 0) }).trigger("blur"), $(function() {
        for (var i = window.location, e = $("ul#sidebarnav a").filter(function() { return this.href == i }).addClass("active").parent().addClass("active");;) {
            if (!e.is("li")) break;
            e = e.parent().addClass("in").parent().addClass("active")
        }
    }), $(function() { $('[data-toggle="tooltip"]').tooltip() }), $(function() { $('[data-toggle="popover"]').popover() }), $(function() { $("#sidebarnav").metisMenu() }), $(".scroll-sidebar").slimScroll({ position: "left", size: "5px", height: "100%", color: "#dcdcdc" }), $(".message-center").slimScroll({ position: "right", size: "5px", color: "#dcdcdc" }), $(".aboutscroll").slimScroll({ position: "right", size: "5px", height: "80", color: "#dcdcdc" }), $(".message-scroll").slimScroll({ position: "right", size: "5px", height: "570", color: "#dcdcdc" }), $(".chat-box").slimScroll({ position: "right", size: "5px", height: "470", color: "#dcdcdc" }), $(".slimscrollright").slimScroll({ height: "100%", position: "right", size: "5px", color: "#dcdcdc" }), $("body").trigger("resize"), $(".list-task li label").click(function() { $(this).toggleClass("task-done") }), $("#to-recover").on("click", function() { $("#loginform").slideUp(), $("#recoverform").fadeIn() }), $('a[data-action="collapse"]').on("click", function(i) { i.preventDefault(), $(this).closest(".card").find('[data-action="collapse"] i').toggleClass("ti-minus ti-plus"), $(this).closest(".card").children(".card-body").collapse("toggle") }), $('a[data-action="expand"]').on("click", function(i) { i.preventDefault(), $(this).closest(".card").find('[data-action="expand"] i').toggleClass("mdi-arrow-expand mdi-arrow-compress"), $(this).closest(".card").toggleClass("card-fullscreen") }), $('a[data-action="close"]').on("click", function() { $(this).closest(".card").removeClass().slideUp("fast") }), $("#monthchart").sparkline([5, 6, 2, 9, 4, 7, 10, 12], { type: "bar", height: "35", barWidth: "4", resize: !0, barSpacing: "4", barColor: "#1e88e5" }), $("#lastmonthchart").sparkline([5, 6, 2, 9, 4, 7, 10, 12], { type: "bar", height: "35", barWidth: "4", resize: !0, barSpacing: "4", barColor: "#0C7CFF" })
    $('#searchcandidate').focus(function(){
        $('.dropdownmenu').addClass('in');
    });
    $("#searchcandidate").focusout(function(){
        $('.dropdownmenu').removeClass('in');
      });
    //   $(document).mouseup(function(e) {
    //       var container = $(".serchboxs");
    //       if (!container.is(e.target) && container.has(e.target).length === 0) 
    //       {
    //         $('.dropdownmenu').removeClass('in');
    //       }
    //   });
});



//  29 - 10 - 2022

(function() {
	function Init() {
		var fileSelect = document.getElementById('file-upload'),
			fileDrag = document.getElementById('file-drag'),
			submitButton = document.getElementById('submit-button');

		fileSelect.addEventListener('change', fileSelectHandler, false);

		// Is XHR2 available?
		var xhr = new XMLHttpRequest();
		if (xhr.upload) 
		{
			// File Drop
			fileDrag.addEventListener('dragover', fileDragHover, false);
			fileDrag.addEventListener('dragleave', fileDragHover, false);
			fileDrag.addEventListener('drop', fileSelectHandler, false);
		}
	}

	function fileDragHover(e) {
		var fileDrag = document.getElementById('file-drag');

		e.stopPropagation();
		e.preventDefault();
		
		fileDrag.className = (e.type === 'dragover' ? 'hover' : 'modal-body file-upload');
	}

	function fileSelectHandler(e) {
		// Fetch FileList object
		var files = e.target.files || e.dataTransfer.files;

		// Cancel event and hover styling
		fileDragHover(e);

		// Process all File objects
		for (var i = 0, f; f = files[i]; i++) {
			parseFile(f);
			uploadFile(f);
		}
	}

	function output(msg) {
		var m = document.getElementById('messages');
		m.innerHTML = msg;
	}

	function parseFile(file) {
		output(
			'<ul>'
			+	'<li>Name: <strong>' + encodeURI(file.name) + '</strong></li>'
			+	'<li>Type: <strong>' + file.type + '</strong></li>'
			+	'<li>Size: <strong>' + (file.size / (1024 * 1024)).toFixed(2) + ' MB</strong></li>'
			+ '</ul>'
		);
	}

	function setProgressMaxValue(e) {
		var pBar = document.getElementById('file-progress');

		if (e.lengthComputable) {
			pBar.max = e.total;
		}
	}

	function updateFileProgress(e) {
		var pBar = document.getElementById('file-progress');

		if (e.lengthComputable) {
			pBar.value = e.loaded;
		}
	}

	function uploadFile(file) {

		var xhr = new XMLHttpRequest(),
			fileInput = document.getElementById('class-roster-file'),
			pBar = document.getElementById('file-progress'),
			fileSizeLimit = 1024;	// In MB
		if (xhr.upload) {
			// Check if file is less than x MB
			if (file.size <= fileSizeLimit * 1024 * 1024) {
				// Progress bar
				pBar.style.display = 'inline';
				xhr.upload.addEventListener('loadstart', setProgressMaxValue, false);
				xhr.upload.addEventListener('progress', updateFileProgress, false);

				// File received / failed
				xhr.onreadystatechange = function(e) {
					if (xhr.readyState == 4) {
						// Everything is good!
						
						// progress.className = (xhr.status == 200 ? "success" : "failure");
						// document.location.reload(true);
					}
				};

				// Start upload
				xhr.open('POST', document.getElementById('file-upload-form').action, true);
				xhr.setRequestHeader('X-File-Name', file.name);
				xhr.setRequestHeader('X-File-Size', file.size);
				xhr.setRequestHeader('Content-Type', 'multipart/form-data');
				xhr.send(file);
			} else {
				output('Please upload a smaller file (< ' + fileSizeLimit + ' MB).');
			}
		}
	}

	// Check for the various File API support.
	if (window.File && window.FileList && window.FileReader) {
		Init();
	} else {
		document.getElementById('file-drag').style.display = 'none';
	}
})();


// & 29 - 10 - 2022