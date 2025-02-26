$(function () {
    function initSlider(sliderId, minField, maxField, minValue, maxValue, step = 1, callback = null) {
        $(sliderId).slider({
            range: true,
            min: minValue,
            max: maxValue,
            values: [minValue, maxValue],
            step: step,
            slide: function (event, ui) {
                $(minField).val(ui.values[0]);
                $(maxField).val(ui.values[1]);
                saveFilters();
            },
            change: function () {
                saveFilters();
            }
        });

        $(minField).val(minValue);
        $(maxField).val(maxValue);
    }

    function saveFilters() {
        let filters = {
            gameName: $("#id-game-name").val(),
            sortBy: $("#sort_by").val(),
            minPlayers: $("#id-min-players").val(),
            maxPlayers: $("#id-max-players").val(),
            minTime: $("#id-min-time").val(),
            maxTime: $("#id-max-time").val(),
            age: $("#age-input").val(),
            tags: $("#id-tags").val(),
            tagSearch: $("#tag-search").val()
        };
        localStorage.setItem("filters", JSON.stringify(filters));
    }

    function loadFilters() {
        let filters = JSON.parse(localStorage.getItem("filters"));
        if (filters) {
            $("#id-game-name").val(filters.gameName);
            $("#sort_by").val(filters.sortBy);
            $("#players-slider").slider("values", [filters.minPlayers, filters.maxPlayers]);
            $("#id-min-players").val(filters.minPlayers);
            $("#id-max-players").val(filters.maxPlayers);
            $("#time-slider").slider("values", [filters.minTime, filters.maxTime]);
            $("#id-min-time").val(filters.minTime);
            $("#id-max-time").val(filters.maxTime);
            $("#age-slider").slider("value", filters.age);
            $("#age-value").text(filters.age);
            $("#age-input").val(filters.age);
            $("#id-tags").val(filters.tags);
            
            $(".tag-btn").removeClass("btn-primary").addClass("btn-outline-primary");
            filters.tags.split(",").forEach(tag => {
                $(".tag-btn[data-tag='" + tag + "']").removeClass("btn-outline-primary").addClass("btn-primary");
            });
            
            $("#tag-search").val(filters.tagSearch);
            updateTagDisplay();
        }
    }

    function updateTagDisplay() {
        let searchValue = $("#tag-search").val().toLowerCase();
        let matchingTags = $(".tag-btn").filter(function () {
            return $(this).text().toLowerCase().includes(searchValue);
        });
        $(".tag-btn").hide();
        matchingTags.slice(0, showAll ? matchingTags.length : 5).show();
        $("#show-more-tags").toggle(matchingTags.length > 5 && !showAll);
        $("#show-less-tags").toggle(showAll);
    }

    let selectedTags = new Set();
    let showAll = false;
    $(".hidden-tag").hide();
    $(".tag-btn").click(function () {
        let tagId = $(this).data("tag");
        selectedTags.has(tagId) ? selectedTags.delete(tagId) : selectedTags.add(tagId);
        $(this).toggleClass("btn-primary btn-outline-primary");
        $("#id-tags").val(Array.from(selectedTags).join(","));
        saveFilters();
    });

    $("#tag-search").on("input", updateTagDisplay);
    $("#show-more-tags").click(() => { showAll = true; updateTagDisplay(); });
    $("#show-less-tags").click(() => { showAll = false; updateTagDisplay(); });

    $("#age-slider").slider({
        range: "min", min: 0, max: 14, value: 6, step: 1,
        slide: function (event, ui) { $("#age-value").text(ui.value); $("#age-input").val(ui.value); saveFilters(); },
        change: saveFilters
    });
    $("#age-value").text($("#age-slider").slider("value"));

    $("#id-game-name").on("input", saveFilters);
    $("#sort_by").on("change", saveFilters);

    $("#reset-button").click(function () {
        localStorage.removeItem("filters");
        $("#id-game-name").val("");
        $("#sort_by").val("name");
        $("#players-slider").slider("values", [1, 20]);
        $("#id-min-players").val(1);
        $("#id-max-players").val(20);
        $("#time-slider").slider("values", [0, 360]);
        $("#id-min-time").val(0);
        $("#id-max-time").val(360);
        $("#age-slider").slider("value", 6);
        $("#age-value").text(6);
        $("#age-input").val(6);
        $(".tag-btn").removeClass("btn-primary").addClass("btn-outline-primary");
        $("#id-tags").val("");
        $("#tag-search").val("");
        showAll = false;
        updateTagDisplay();
    });

    initSlider("#players-slider", "#id-min-players", "#id-max-players", 1, 20);
    initSlider("#time-slider", "#id-min-time", "#id-max-time", 0, 360, 5);
    loadFilters();
});
