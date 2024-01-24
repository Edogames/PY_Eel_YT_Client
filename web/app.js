function Search(){
    const query = document.getElementById("search-input").value;
    eel.search_videos(query)().then(result => {
        // Display videos in the UI
        const results = document.getElementById("results");
        if(document.getElementById("morebtn")){
            document.getElementById("morebtn").remove();
        }
        results.innerHTML = ""; // Clear previous results
        for (const video of result) {
            const videoElement = document.createElement("div");
            videoElement.innerHTML = `
                <div class="video-container" onClick="handleThumbnailClick('${video.id.videoId}')">
                    <img src="${video.snippet.thumbnails.high.url}">
                    <h3>${video.snippet.title}</h3>
                </div>
            `;
            results.appendChild(videoElement);
        }
        results.innerHTML += `<button onClick="" id="morebtn">More</button>`;
    })
    .catch(error => {
        console.error(error);
    });
}

eel.expose(set_video_source_and_play);

function set_video_source_and_play(embedHTML) {
    const player = document.querySelector("#video-container");
    return player.innerHTML = embedHTML;
}

// Example: When a thumbnail is clicked
async function handleThumbnailClick(videoId) {
    eel.play_video(videoId);
}

document.getElementById("search-button").addEventListener("click", function() {
    Search();
});

Search();
