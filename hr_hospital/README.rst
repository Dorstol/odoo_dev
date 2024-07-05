======================
Hospital Management
======================

Overview
========
The Hospital Management module is designed to help manage the operations of a hospital, including the management of doctors, patients, diseases, and visits. This module is aimed at providing an efficient system for tracking and organizing hospital-related data.

Features
========
- Manage doctors with their specialization.
- Manage patients with their personal information and assigned doctors.
- Maintain a list of diseases.
- Track patient visits.

Installation
============
1. Clone the repository into your Odoo custom addons directory:

    .. code-block:: bash

        git clone <repository_url> path_to_odoo_addons/hospital_management

2. Update the Odoo configuration file to include the custom addons directory:

    .. code-block:: ini

        addons_path = path_to_odoo_addons/hospital_management

3. Restart the Odoo server:

    .. code-block:: bash

        ./odoo-bin -c /etc/odoo/odoo.conf

4. Install the module through the Odoo Apps interface.

Configuration
=============
No additional configuration is needed after installation.

Usage
=====
1. Navigate to the "Hospital Management" menu in the Odoo interface.
2. Use the "Doctors" submenu to manage doctor records.
3. Use the "Patients" submenu to manage patient records.
4. Use the "Diseases" submenu to manage disease records.
5. Use the "Visits" submenu to manage and track patient visits.

Demo Data
=========
The module includes demo data for initial testing purposes. The following demo records are provided:
- Three doctors with different specializations.
- Three patients assigned to different doctors.
- Three diseases.

Known Issues
============
None at the moment.

Contributing
============
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with detailed description of the changes.

License
=======
This module is licensed under the MIT License. See the LICENSE file for details.

Contact
=======
For any questions or support, please contact us at support@example.com.
