#!/bin/bash
set -e

echo "⏳ Waiting for Postgres..."
until pg_isready -h odoo-db -U odoo; do
  sleep 2
done

echo "🚀 Initializing database..."
odoo -c /etc/odoo/odoo.conf -d odoo -i base,web,operator --without-demo=all --stop-after-init || true

echo "🧪 Running tests for module 'operator'..."
odoo -c /etc/odoo/odoo.conf -d odoo -i operator --test-enable --stop-after-init || true

echo "✅ Starting Odoo..."
exec odoo -c /etc/odoo/odoo.conf -d odoo
