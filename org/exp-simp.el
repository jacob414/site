(setq make-backup-files nil)

(require 'ox-html)

(defun org-export-all-org-files-in-directory ()
  "Export all org files in the current directory as HTML without a table of contents or a footer."
  (interactive)
  (let ((org-export-with-toc nil)
        (org-html-postamble nil))
    (dolist (org-file (directory-files default-directory t "\\.org$"))
      (with-current-buffer (find-file-noselect org-file)
        (org-html-export-to-html)))))

(org-export-all-org-files-in-directory)
