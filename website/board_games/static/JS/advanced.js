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

    // Affichage des tags cachés
    $("#show-more-tags").click(function () {
        $(".hidden-tag").fadeIn(); // Affiche les tags cachés
        $(this).hide(); // Cache le bouton "Afficher plus"
        $("#show-less-tags").show(); // Affiche le bouton "Voir moins"
    });

    // Repli des tags
    $("#show-less-tags").click(function () {
        $(".hidden-tag").fadeOut(function () {
            $(this).addClass("hidden-tag"); // Réapplique la classe pour le masquage
        });
        $(this).hide(); // Cache le bouton "Voir moins"
        $("#show-more-tags").show(); // Réaffiche le bouton "Afficher plus"
    });
    // Recherche dynamique des tags
    $("#tag-search").on("input", function () {
        let searchValue = $(this).val().toLowerCase();

        $(".tag-btn").each(function () {
            let tagText = $(this).text().toLowerCase();

            if (tagText.includes(searchValue)) {
                $(this).show(); // Affiche les tags correspondants
            } else {
                $(this).hide(); // Masque les tags non pertinents
            }
        });

        // Ajuster l'affichage des boutons "Afficher plus" et "Voir moins"
        if ($(".tag-btn:visible").length > 5) {
            $("#show-more-tags").hide();
            $("#show-less-tags").show();
        } else {
            $("#show-more-tags").show();
            $("#show-less-tags").hide();
        }
    });
});

/*
$(document).ready(function () {
    let selectedTags = new Set(); // Stocke les tags sélectionnés

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
});
*/