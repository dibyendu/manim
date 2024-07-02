Ray in Ellipse
================

.. admonition:: Ray in Ellipse

   .. video:: _static/video/ellipse.mp4
      :loop:
      :autoplay:
      :class: mainm-video
   .. literalinclude:: ../code/ellipse.py
     :language: python
     :class: mainm-code
   .. literalinclude:: ../code/ellipse.py
     :language: python
     :class: mainm-editor
   .. raw:: html

      <div id='app'></div>
      <script>
         document.addEventListener('DOMContentLoaded', function(event) {
            const editors = document.getElementsByClassName('mainm-editor')
            for (let i = 0; i < editors.length; ++i) {
               editors[i].setAttribute('data-manim-binder', '')
               editors[i].setAttribute('data-manim-classname', 'EllipseRay')
            }
            initManimBinder({ branch: 'main' })
         })
      </script>