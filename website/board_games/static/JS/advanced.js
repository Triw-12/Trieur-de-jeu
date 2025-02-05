$(function () {
	// Initialisation du slider pour le nombre de joueurs
	const minPlayers = 1;  // Valeur minimale du slider
	const maxPlayers = 20; // Valeur maximale du slider

	$("#players-slider").slider({
	    range: true,
	    min: minPlayers,
	    max: maxPlayers,
	    values: [minPlayers, maxPlayers],
	    slide: function (event, ui) {
		   // Mise à jour des champs min-players et max-players
		   $("#id-min-players").val(ui.values[0]);
		   $("#id-max-players").val(ui.values[1]);
	    }
	});

	// Initialisation des valeurs des champs à celles du slider
	$("#id-min-players").val($("#players-slider").slider("values", 0));
	$("#id-max-players").val($("#players-slider").slider("values", 1));
});

 $(function () {
	// Initialisation du slider pour le nombre de joueurs
	const minTime = 0;  // Valeur minimale du slider
	const maxTime = 360; // Valeur maximale du slider

	$("#time-slider").slider({
	    range: true,
	    min: minTime,
	    max: maxTime,
	    values: [minTime, maxTime],
		step: 5,
	    slide: function (event, ui) {
		   // Mise à jour des champs min-players et max-players
		   $("#id-min-time").val(ui.values[0]);
		   $("#id-max-time").val(ui.values[1]);
	    }
	});

	// Initialisation des valeurs des champs à celles du slider
	$("#id-min-time").val($("#time-slider").slider("values", 0));
	$("#id-max-time").val($("#time-slider").slider("values", 1));
});

$(document).ready(function () {
    let selectedTags = new Set(); // Stocke les tags sélectionnés
    let showAll = false; // Indique si on est en mode large (true) ou réduit (false)

    // Masquer les tags supplémentaires au démarrage
    $(".hidden-tag").hide();

    // Gestion de la sélection des tags
    $(".tag-btn").click(function () {
        let tagId = $(this).data("tag");

        if (selectedTags.has(tagId)) {
            selectedTags.delete(tagId);
            $(this).removeClass("btn-primary").addClass("btn-outline-primary");
        } else {
            selectedTags.add(tagId);
            $(this).removeClass("btn-outline-primary").addClass("btn-primary");
        }

        $("#id-tags").val(Array.from(selectedTags).join(","));
    });

    // Fonction pour afficher les tags en fonction du mode actuel
    function updateTagDisplay() {
        let searchValue = $("#tag-search").val().toLowerCase();
        let matchingTags = [];

        // Filtrer les tags selon la recherche
        $(".tag-btn").each(function () {
            let tagText = $(this).text().toLowerCase();
            if (tagText.includes(searchValue)) {
                matchingTags.push(this);
            } else {
                $(this).hide();
            }
        });

        // Affichage selon le mode actuel
        $(".tag-btn").hide(); // On cache tous les tags avant d'afficher les bons

        if (showAll) {
            // Mode large → afficher tous les tags correspondant à la recherche
            matchingTags.forEach(tag => $(tag).show());
            $("#show-more-tags").hide();
            $("#show-less-tags").toggle(matchingTags.length > 5);
        } else {
            // Mode réduit → afficher seulement 5 résultats max
            matchingTags.slice(0, 5).forEach(tag => $(tag).show());
            $("#show-more-tags").toggle(matchingTags.length > 5);
            $("#show-less-tags").hide();
        }
    }

    // Recherche dynamique des tags
    $("#tag-search").on("input", function () {
        updateTagDisplay();
    });

    // Affichage des tags cachés → Passe en mode large
    $("#show-more-tags").click(function () {
        showAll = true;
        $(".tag-btn").show(); // Afficher tous les tags d'abord
        updateTagDisplay(); // Ensuite appliquer la recherche
        $(this).hide();
        $("#show-less-tags").show();
    });

    // Repli des tags → Passe en mode réduit
    $("#show-less-tags").click(function () {
        showAll = false;
        updateTagDisplay(); // Appliquer la recherche d'abord, puis réduire à 5
        $(this).hide();
        $("#show-more-tags").show();
    });
});
