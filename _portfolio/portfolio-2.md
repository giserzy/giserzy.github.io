---
title: "Inequality"
excerpt: "Sensing noise exposure and its inequality based on noise complaint data through vision-language hybrid method"
collection: portfolio
collection: portfolio
header:
  teaser: "/images/cam.png"
---

The differences between the quite and noise scenario.

Ref: Zhang Y, Kwan M P, Ma H. Sensing noise exposure and its inequality based on noise complaint data through vision-language hybrid method[J]. Applied Geography, 2024, 171: 103369.

<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
.container {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  user-select: none;
}

.image-wrapper {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.image-after {
  width: 100%;
  display: block;
}

.image-before {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  clip-path: inset(0 50% 0 0);
}

.slider-handle {
  position: absolute;
  top: 0;
  left: 50%;
  width: 4px;
  height: 100%;
  background: white;
  cursor: ew-resize;
  transform: translateX(-50%);
  box-shadow: 0 0 5px rgba(0,0,0,0.5);
}

.slider-button {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: white;
  cursor: ew-resize;
  box-shadow: 0 0 5px rgba(0,0,0,0.5);
}

.slider-button::before,
.slider-button::after {
  content: '';
  position: absolute;
  width: 10px;
  height: 2px;
  background: #555;
  top: 50%;
}

.slider-button::before {
  transform: translateY(-50%) rotate(-45deg);
  left: 8px;
}

.slider-button::after {
  transform: translateY(-50%) rotate(45deg);
  right: 8px;
}
</style>
</head>
<body>

<div class="container">
  <div class="image-wrapper">
    <!-- 处理后的图片 -->
    <img class="image-after" src="/images/camnoise.jpg" alt="Processed Image">
    
    <!-- 处理前的图片 -->
    <img class="image-before" src="/images/quite.jpg" alt="Original Image">
    
    <div class="slider-handle">
      <div class="slider-button"></div>
    </div>
  </div>
</div>

<script>
const container = document.querySelector('.container');
const imageBefore = document.querySelector('.image-before');
const sliderHandle = document.querySelector('.slider-handle');
let isDragging = false;

function updateClip(percentage) {
  imageBefore.style.clipPath = `inset(0 ${100 - percentage}% 0 0)`;
  sliderHandle.style.left = `${percentage}%`;
}

function handleDrag(e) {
  if (!isDragging) return;
  
  const rect = container.getBoundingClientRect();
  let x = e.clientX - rect.left;
  
  // 确保滑块在容器范围内
  x = Math.max(0, Math.min(x, rect.width));
  
  const percentage = (x / rect.width) * 100;
  updateClip(percentage);
}

function handleTouch(e) {
  if (!isDragging) return;
  
  const rect = container.getBoundingClientRect();
  let x = e.touches[0].clientX - rect.left;
  
  x = Math.max(0, Math.min(x, rect.width));
  
  const percentage = (x / rect.width) * 100;
  updateClip(percentage);
}

// 鼠标事件
sliderHandle.addEventListener('mousedown', () => {
  isDragging = true;
});

window.addEventListener('mousemove', handleDrag);
window.addEventListener('mouseup', () => {
  isDragging = false;
});

// 触摸事件
sliderHandle.addEventListener('touchstart', (e) => {
  isDragging = true;
  handleTouch(e);
});

window.addEventListener('touchmove', handleTouch, { passive: false });
window.addEventListener('touchend', () => {
  isDragging = false;
});

// 防止拖动时选中文本
container.addEventListener('dragstart', (e) => {
  e.preventDefault();
});
</script>

</body>
</html>