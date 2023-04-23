class ScrollHandler {
    constructor(){
        this.water = document.getElementById("violet-water");
        this.sun = document.getElementById("sun");
        this.mountains_behind = document.getElementById("mountains-behind");
        this.mountain_front = document.getElementById("mountain-front");
        this.feed_text = document.getElementById("feed");
        this.btn = document.getElementById("btn");

        window.addEventListener("scroll", () => {
            let value = window.scrollY;
            this.sun.style.top = value * 0.85 + "px";
            this.mountain_front.style.top = value * 0.3 + "px";
            this.mountains_behind.style.top = value * 0.5 + "px";
            this.feed_text.style.marginRight = value * 5 + "px";
            this.btn.style.marginTop = value * 1.5 + "px";
        });

    }
}

const scrolHandler = new ScrollHandler();