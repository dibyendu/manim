Recursive Circle
================

.. admonition:: Recursive Circle

   .. video:: _static/video/circle.mp4
      :loop:
      :autoplay:
      :class: mainm-video
   .. literalinclude:: ../code/circle.py
     :language: python
     :class: mainm-code
   .. literalinclude:: ../code/circle.py
     :language: python
     :class: mainm-editor
   .. raw:: html

      <div id='app'></div>
      <script>
         document.addEventListener('DOMContentLoaded', function(event) {
            const editors = document.getElementsByClassName('mainm-editor')
            for (let i = 0; i < editors.length; ++i) {
               editors[i].setAttribute('data-manim-binder', '')
               editors[i].setAttribute('data-manim-classname', 'RecursiveCircle')
            }
            initManimBinder({ branch: 'main' })
         })
      </script>