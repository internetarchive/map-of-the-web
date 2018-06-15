"""motw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from . import view
from django.conf.urls import url

urlpatterns = [
    url(r'^$', view.test),
]
